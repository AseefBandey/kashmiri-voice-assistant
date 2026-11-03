## Description
<!-- Provide a concise summary of the changes made in this pull request and the motivation behind them. -->

## Associated Jira Issue / Ticket
- Jira Ticket: [e.g., `ASR-101`](https://jira.example.com/browse/ASR-101)

## Type of Change
- [ ] New feature (e.g., acoustic modeling, feature extraction, normalization)
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] Pipeline / Config update (training params, dataset preprocessing scripts)
- [ ] Documentation update
- [ ] Unit / Integration test addition

## Pull Request Checklist
Please verify the following before requesting a review:

### 1. Jira & Traceability
- [ ] PR title follows conventional naming (e.g., `feat(asr): add Kashmiri orthographic normalizer [ASR-101]`)
- [ ] Jira ticket or issue link is attached above

### 2. Testing & Quality
- [ ] Unit/integration tests added or updated for new changes
- [ ] All tests pass locally (`PYTHONPATH=src python3 -m unittest discover tests` or `pytest`)
- [ ] Code formatting and lint checks verified

### 3. Documentation
- [ ] Code is documented with clear docstrings and comments where appropriate
- [ ] Relevant documentation in `docs/` or `README.md` has been updated

### 4. Data Privacy, Secrets & Model Weights Check
- [ ] **No credentials or secrets** (`.env`, API tokens) are committed
- [ ] **No private audio recordings or local raw datasets** (`.wav`, `.mp3`, `.flac`, etc.) are committed
- [ ] **No large model weights or checkpoints** (`.pt`, `.bin`, `.safetensors`) are committed
- [ ] Staged files checked via `git status` / `git diff --cached --stat`
