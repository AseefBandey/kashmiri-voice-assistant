# Kashmiri Voice Assistant 

A professional speech recognition and orthographic normalization pipeline for Kashmiri speech processing.

---

## 📌 Project Purpose

The Automatic Speech Recognition (ASR) workstream focuses on building a reproducible Kashmiri speech-to-text system:
- **Acoustic Modeling**: Fine-tuning multi-lingual speech models on Kashmiri speech.
- **Orthographic Normalization**: Standardizing Kashmiri Perso-Arabic unicode representations and diacritics.
- **Standardized Evaluation**: Benchmarking models using Word Error Rate (WER) and Character Error Rate (CER).

---

## Project Architecture


```mermaid
flowchart LR
    A["Kashmiri Voice Input"] --> B["Audio Processing"]
    B --> C["Kashmiri ASR<br/>(Speech-to-Text)"]
    C --> D["NLP / LLM Processing"]
    D --> E["Response Generation"]
    E --> F["Kashmiri Text-to-Speech"]
    F --> G["Spoken Kashmiri Output"]

    classDef green fill:#1c4436,stroke:#1c4436,color:#fff;
    classDef brown fill:#5a3825,stroke:#5a3825,color:#fff;
    classDef maroon fill:#6f263e,stroke:#6f263e,color:#fff;

    class A,G green;
    class B,F brown;
    class C,D,E maroon;
```

---

## 📂 Project Structure

```text
kashmiri-voice-assistant/
├── README.md
├── .gitignore
├── .env.example
├── pyproject.toml          # or requirements.txt
├── docs/
├── configs/
├── data/                   # local/approved data only; ignored by Git
├── notebooks/
├── src/
│   └── voice_assistant/
│       └── asr/
├── scripts/
├── reports/
└── tests/
```

---

## 🛠️ Setup Instructions

### 1. Prerequisites
- Python 3.10+
- Git

### 2. Environment Setup

```bash
# Clone repository
git clone https://github.com/AseefBandey/kashmiri-voice-assistant.git
cd kashmiri-voice-assistant

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate

# Install dependencies in editable mode
pip install --upgrade pip
pip install -e ".[dev]"

# Configure local environment variables
cp .env.example .env
```

### 3. Verification Check
Run the test suite to confirm your local environment and normalizer are functioning:
```bash
PYTHONPATH=src python3 -m unittest discover tests
# Or with pytest:
pytest
```

---

## 🤝 Contribution & Pull Request Rules

1. **No Direct Commits to `main`**:
   - The `main` branch is protected.
   - All contributions must be made through a feature branch and merged via Pull Request.
2. **Branch Naming Standard**:
   - `feat/<jira-id>-<description>`
   - `fix/<jira-id>-<description>`
   - `docs/<jira-id>-<description>`
3. **Pull Request Checklist**:
   - [ ] Linked Jira issue (e.g. `ASR-101`)
   - [ ] Unit tests pass locally
   - [ ] Documentation updated
   - [ ] **Data & Privacy Check**: No credentials, private audio recordings, unapproved datasets, or model weights committed.

---

## 🔒 Security & Privacy Notice

> [!CAUTION]
> **Strict Policy**: Never commit audio datasets, private recordings, model weights (`.pt`, `.bin`, `.safetensors`), credentials, or `.env` files to this repository. All sensitive artifacts are excluded via `.gitignore`.
