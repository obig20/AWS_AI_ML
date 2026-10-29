# AWS AI/ML Course Repository

A collection of weekly projects for the AWS AI/ML course, progressing from core data processing to semantic search and beyond.

## Repository Structure

```
AWS_AI_ML/
├── week1/   # Data processing with NumPy and Pandas
├── week2/   # Mini Semantic Search Lab
└── README.md
```

## Week 1 — Data Processing

A small Python data-processing application that loads, cleans, and processes tabular data using NumPy.

**Features**
- Load datasets from CSV or JSON
- Clean missing values and remove empty columns
- Cast columns to numeric/int types
- Convert cleaned rows to NumPy arrays
- Run NumPy-based processing: statistics, z-score normalization, outlier flagging

**Files**
- `data_processing.py` — core pipeline (`load_dataset`, `clean_missing`, `clean_types`, `to_array`, `process`, `run_pipeline`)
- `sample.csv` — sample input data
- `notebook.ipynb` — exploratory notebook
- `requirements.txt` — dependencies
- `setup_venv.ps1` — Windows virtual environment setup

**Run**
```bash
python data_processing.py demo
# or
python data_processing.py path/to/data.csv
```

## Week 2 — Mini Semantic Search Lab

A mini semantic search engine for FAQs: loads FAQ data, cleans it, computes NumPy statistics, generates embeddings with Sentence Transformers, stores them in ChromaDB, and retrieves the top 3 most similar FAQs for a query.

See `week2/week-02-mini-semantic-search/README.md` for full details.

## Getting Started

```bash
# Week 1
cd week1
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Week 2
cd ..\week2\week-02-mini-semantic-search
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Tech Stack

- Python 3.8+
- NumPy, Pandas
- Jupyter
- Sentence Transformers, ChromaDB (Week 2)

## License

Educational use.
" filePath">
C:\Users\Noha\OneDrive\Desktop\Amazon AI\README.md