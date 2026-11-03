# Final Year Engineering AI/ML Project

A collaborative, reproducible AI/ML engineering codebase for the final-year research project.

---

## 📌 Repository Purpose & Objectives

This repository serves as the shared codebase for research, experimentation, modeling, and evaluation. It is structured to ensure:
- **Reproducibility:** Versioned code, pinned environments, and clear pipeline configs.
- **Collaboration:** Standardized branch workflows, code reviews, and PR templates.
- **Data Governance & Privacy:** Rigorous protection ensuring no private audio recordings, unapproved datasets, model checkpoints, or credentials enter Git history.

---

## 📂 Repository Structure

```text
FinalYear/
├── .github/
│   └── pull_request_template.md  # PR checklist for Jira, tests, docs & data checks
├── configs/                      # Configuration files (YAML, JSON) for models & pipelines
│   └── config.yaml.example       # Template config file
├── data/                         # Local datasets (git-ignored, see data/README.md)
│   ├── raw/                      # Original, immutable datasets
│   ├── processed/                # Preprocessed feature sets
│   └── README.md                 # Data privacy & storage policy
├── docs/                         # Documentation, research notes, architecture diagrams
├── notebooks/                    # Jupyter notebooks for EDA and rapid prototyping
├── reports/                      # Generated figures, evaluation tables, and final report drafts
├── scripts/                      # Standalone automation scripts (data fetch, benchmark runs)
├── src/                          # Reusable core Python package / source modules
│   └── __init__.py
├── tests/                        # Unit and integration test suite
│   ├── __init__.py
│   └── test_placeholder.py
├── .env.example                  # Template for local environment variables & tokens
├── .gitignore                    # Exclusion rules for secrets, weights, audio & data
├── CONTRIBUTING.md                # Collaboration, branch naming, and review rules
├── pyproject.toml                # Modern Python package specification (PEP 621)
├── requirements.txt              # Core runtime dependencies
├── requirements-dev.txt          # Development, testing, and linting dependencies
└── README.md                     # Project overview and setup guide
```

---

## 🛠️ Environment & Dependency Setup

You can set up your local development environment using standard `venv` with `requirements.txt` or editable `pyproject.toml`.

### 1. Prerequisites
- Python 3.10+ (Recommended: Python 3.11 / 3.12 / 3.14)
- Git

### 2. Quickstart Setup

```bash
# 1. Clone repository
git clone https://github.com/<ORG_OR_USERNAME>/FinalYear.git
cd FinalYear

# 2. Create Python virtual environment
python3 -m venv .venv

# 3. Activate virtual environment
source .venv/bin/activate       # On Linux/macOS
# .venv\Scripts\activate        # On Windows Command Prompt / PowerShell

# 4. Upgrade pip and install dependencies
pip install --upgrade pip

# Option A: Using requirements files
pip install -r requirements-dev.txt

# Option B: Using pyproject.toml in editable mode
pip install -e ".[dev]"

# 5. Configure environment variables
cp .env.example .env
```

### 3. Verify Setup
Run the test suite to verify your setup:
```bash
pytest
```

---

## 🤝 Contribution & Collaboration Rules

To ensure code stability and smooth peer collaboration:
1. **Never commit directly to `main`**.
2. **Branch naming:** Follow `feat/<issue-id>-<description>`, `fix/...`, or `docs/...`.
3. **Pull Requests:** Open a PR against `main` and complete the **PR Checklist** (linked Jira ticket, test pass, no committed secrets/audio/weights).
4. **Peer Review:** Every PR requires approval from a collaborator before merging.

For full step-by-step contribution instructions, see [CONTRIBUTING.md](file:///home/dtm1n/Downloads/FinalYear/CONTRIBUTING.md).

---

## 🔒 Data & Security Governance

This project enforces strict policies regarding data and artifacts:
- **Audio Files:** Any `.wav`, `.mp3`, `.flac`, etc., are strictly ignored by `.gitignore` and must never be committed.
- **Model Checkpoints:** Large `.pt`, `.pth`, `.safetensors`, `.bin` files are stored in external artifact storage, not Git.
- **Secrets:** API keys, tokens, and credentials must live exclusively in `.env` (which is never tracked).

To audit your staged files before committing:
```bash
git status
git diff --cached --stat
```

---

## 📋 7-Day Deliverables & Milestone Tracker

- [x] **Day 1:** Shared GitHub repository setup, invite Person A, README.md & .gitignore.
- [x] **Day 2:** Python dependency/environment structure (`requirements.txt` + `pyproject.toml`) and folder structure.
- [x] **Day 3:** Document branch naming and PR rules; avoid direct commits to `main` (`CONTRIBUTING.md`).
- [x] **Day 4:** PR checklist for Jira links, tests, documentation, and data/privacy checks (`.github/pull_request_template.md`).
- [ ] **Day 5:** Person A clones repo, follows setup, branches, and opens test PR.
- [ ] **Day 6:** Resolve setup issues reported by Person A.
- [ ] **Day 7:** Final audit confirming no secrets, private audio, unapproved datasets, or weights are tracked.
