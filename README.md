# Kashmiri Voice Assistant — ASR Workstream

A professional speech recognition and orthographic normalization pipeline for low-resource Kashmiri speech processing.

---

## 📌 Project Purpose

The Automatic Speech Recognition (ASR) workstream focuses on building a reproducible Kashmiri speech-to-text system:
- **Acoustic Modeling**: Fine-tuning multi-lingual speech models on Kashmiri speech.
- **Orthographic Normalization**: Standardizing Kashmiri Perso-Arabic unicode representations and diacritics.
- **Standardized Evaluation**: Benchmarking models using Word Error Rate (WER) and Character Error Rate (CER).
- **Data Governance**: Enforcing strict protocols to safeguard audio recordings, proprietary datasets, and credentials.

---

## 🏛 Architecture

```mermaid
flowchart LR
    A["Kashmiri Audio (16 kHz WAV)"] --> B["Acoustic Preprocessing"]
    B --> C["Acoustic Model (ASR)"]
    C --> D["Token Decoding"]
    D --> E["Kashmiri Normalizer"]
    E --> F["Kashmiri Text"]
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
