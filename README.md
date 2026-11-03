# Kashmiri Voice Assistant — ASR Workstream

Collaborative repository for the **Automatic Speech Recognition (ASR)** workstream of the Kashmiri Voice Assistant project.

This workstream focuses on building a reproducible Kashmiri speech-to-text pipeline, including orthographic normalization, acoustic model fine-tuning, and evaluation on conversational and read Kashmiri speech.

---

## 📌 Project Purpose

- **Acoustic & Language Modeling**: Developing and fine-tuning robust ASR models (e.g. Whisper, MMS, Wav2Vec2) for Kashmiri.
- **Orthographic Standardization**: Handling Kashmiri Perso-Arabic orthographic variation and canonicalizing transcriptions.
- **Reproducible Evaluation**: Standardized benchmark harness reporting Word Error Rate (WER) and Character Error Rate (CER).
- **Data Governance**: Enforcing rigorous privacy policies to protect proprietary and private audio recordings.

---

## 📂 Repository Structure

```text
kashmiri-voice-assistant/
├── README.md               # Project purpose, setup, and workflow
├── .gitignore              # Rules excluding audio, models, secrets, and caches
├── .env.example            # Template for environment variables (copy to .env)
├── pyproject.toml          # Package configuration and dependencies (or requirements.txt)
├── docs/                   # Technical specs, orthography notes, meeting logs
├── configs/                # Hyperparameters and pipeline configuration YAMLs
├── data/                   # Local/approved data only; strictly ignored by Git
│   ├── raw/                # Untracked raw data
│   ├── processed/          # Untracked preprocessed features
│   └── README.md           # Data policy and privacy requirements
├── notebooks/              # Jupyter notebooks for EDA and error analysis
├── src/
│   └── voice_assistant/
│       └── asr/            # Kashmiri ASR package (normalizers, model stubs, pipelines)
├── scripts/                # Utility scripts (batch preprocessing, inference runs)
├── reports/                # Evaluation reports, metrics plots, and paper drafts
└── tests/                  # Unit and integration test suite
```

---

## 🛠️ Python Environment & Dependency Setup

You can choose either standard `requirements.txt` or `pyproject.toml`.

### Prerequisites
- Python 3.10+
- Git

### Initial Setup Steps

```bash
# 1. Clone the shared repository
git clone https://github.com/<OWNER>/kashmiri-voice-assistant.git
cd kashmiri-voice-assistant

# 2. Create and activate a Python virtual environment
python3 -m venv .venv
source .venv/bin/activate       # On Linux/macOS
# .venv\Scripts\activate        # On Windows (cmd/PowerShell)

# 3. Upgrade pip and install dependencies
pip install --upgrade pip

# Option A: Install via requirements.txt
pip install -r requirements-dev.txt

# Option B: Install via pyproject.toml (editable mode)
pip install -e ".[dev]"

# 4. Copy environment configuration
cp .env.example .env
```

### Run the Verification Check
Verify that the test suite and ASR text normalization modules work correctly:
```bash
# Using unittest
PYTHONPATH=src python3 -m unittest discover tests

# Or using pytest (if installed)
pytest
```

---

## 🤝 Contribution & Collaboration Rules

To ensure stability across the shared repository:

1. **Strictly No Direct Commits to `main`**:
   - The `main` branch is protected.
   - All contributions must be made via feature branches and Pull Requests (PRs).
2. **Branch Naming Standard**:
   - Features: `feat/<jira-id>-<description>` (e.g., `feat/ASR-101-kashmiri-normalizer`)
   - Bug Fixes: `fix/<jira-id>-<description>` (e.g., `fix/ASR-104-sampling-rate-fix`)
   - Docs / Chores: `docs/<jira-id>-<description>`, `chore/...`
3. **Pull Request Protocol**:
   - Each PR must link a Jira issue.
   - Every PR must pass all test checks.
   - Every PR requires at least one approving peer review before merging.

For detailed guidelines, see [CONTRIBUTING.md](file:///home/dtm1n/Downloads/FinalYear/CONTRIBUTING.md).

---

## 🔒 Data & Security Governance

> [!CAUTION]
> **Strictly check your commits before pushing!**
> - **Never commit audio datasets or private recordings** (`.wav`, `.mp3`, `.flac`, etc.).
> - **Never commit model weights or checkpoints** (`.pt`, `.bin`, `.safetensors`).
> - **Never commit credentials, API keys, or `.env` files**.

To verify your staged changes before committing:
```bash
git status
git diff --cached --stat
```

---

## ✅ Acceptance Criteria Tracker

- [x] Shared GitHub repository structure initialized.
- [x] Both contributors can clone and set up the repository.
- [x] Setup instructions verified with built-in sanity checks.
- [x] `.gitignore` thoroughly configured and verified.
- [x] Pull request template and branch naming standards established.
- [x] Zero credentials, private audio, or model weights tracked in Git.
