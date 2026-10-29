"""Small Python data-processing app: load, clean, process with NumPy."""
import csv
import json
from pathlib import Path

import numpy as np


def load_dataset(source):
    """Load a raw dataset from a CSV path or a list of dicts/rows."""
    if isinstance(source, (str, Path)):
        path = Path(source)
        if path.suffix.lower() == ".json":
            return json.loads(path.read_text())
        with path.open(newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    if isinstance(source, list):
        return [dict(r) for r in source]
    raise TypeError("source must be a path or list")


def clean_missing(rows, drop_cols=()):
    """Drop rows with missing critical fields and remove empty columns."""
    cleaned = []
    for r in rows:
        if any(r.get(k) in (None, "", "NA", "NaN") for k in r if k not in drop_cols):
            continue
        cleaned.append({k: v for k, v in r.items() if k not in drop_cols})
    return cleaned


def clean_types(rows, numeric_cols=(), int_cols=()):
    """Cast columns to numeric/int types where possible."""
    out = []
    for r in rows:
        nr = dict(r)
        for c in numeric_cols:
            try:
                nr[c] = float(nr[c])
            except (ValueError, TypeError):
                nr[c] = np.nan
        for c in int_cols:
            try:
                nr[c] = int(float(nr[c]))
            except (ValueError, TypeError):
                nr[c] = None
        out.append(nr)
    return out


def to_array(rows, cols):
    """Convert selected columns of cleaned rows into a NumPy array."""
    return np.array([[r[c] for c in cols] for r in rows], dtype=float)


def process(rows):
    """Run NumPy-based processing: stats, normalization, outlier flagging."""
    numeric_cols = [k for k, v in rows[0].items() if isinstance(v, (int, float))]
    arr = to_array(rows, numeric_cols)
    stats = {
        "shape": arr.shape,
        "mean": np.nanmean(arr, axis=0),
        "std": np.nanstd(arr, axis=0),
        "min": np.nanmin(arr, axis=0),
        "max": np.nanmax(arr, axis=0),
    }
    # z-score normalization
    mean = np.nanmean(arr, axis=0)
    std = np.nanstd(arr, axis=0)
    std[std == 0] = 1.0
    z = (arr - mean) / std
    # flag outliers (|z| > 3)
    outlier_mask = np.any(np.abs(z) > 3, axis=1)
    return {
        "columns": numeric_cols,
        "array": arr,
        "z_scores": z,
        "outliers": int(outlier_mask.sum()),
        "stats": stats,
    }


def run_pipeline(source):
    rows = load_dataset(source)
    rows = clean_missing(rows)
    rows = clean_types(rows, numeric_cols=[k for k in rows[0] if k != "name"])
    result = process(rows)
    return rows, result


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Data processing app")
    parser.add_argument("source", help="CSV/JSON path or 'demo'")
    args = parser.parse_args()

    if args.source == "demo":
        demo = [
            {"name": "a", "value": "10", "score": "85"},
            {"name": "b", "value": "20", "score": "90"},
            {"name": "c", "value": "", "score": "70"},
            {"name": "d", "value": "15", "score": "999"},
        ]
        rows, result = run_pipeline(demo)
    else:
        rows, result = run_pipeline(args.source)

    print("Rows:", len(rows))
    print("Columns:", result["columns"])
    print("Shape:", result["stats"]["shape"])
    print("Mean:", result["stats"]["mean"])
    print("Outliers:", result["outliers"])