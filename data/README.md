# Data Directory Policy

> [!CAUTION]
> **NEVER commit raw, unapproved datasets, private audio files, or sensitive recordings to this repository.**

## Directory Structure
- `data/raw/`: Place original immutable raw datasets here locally. (Ignored by Git)
- `data/interim/`: Intermediate transformed data. (Ignored by Git)
- `data/processed/`: Final datasets used for training/benchmarking. (Ignored by Git)

## How to Obtain & Store Data
1. Download datasets from authorized project storage or cloud buckets (e.g. Google Drive, S3, Hugging Face Hub private dataset).
2. Store your local credentials in `.env` (copy from `.env.example`).
3. Run data download/preparation scripts located in `scripts/`.
