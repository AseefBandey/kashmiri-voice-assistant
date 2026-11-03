## Description
<!-- Provide a concise summary of the changes made in this pull request and the motivation behind them. -->

## Associated Issue / Jira Ticket
- Jira Ticket / Issue: [e.g., `FYP-101`](https://jira.example.com/browse/FYP-101)

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing code not to work as expected)
- [ ] Documentation update
- [ ] Experiment / Analysis pipeline update

## Pull Request Checklist
Please verify the following before requesting a review:

### 1. Jira & Traceability
- [ ] PR title follows conventional naming (e.g., `feat(audio): add feature extraction [FYP-101]`)
- [ ] Jira ticket or issue link is attached above

### 2. Testing & Quality
- [ ] Unit/integration tests added or updated for new changes
- [ ] All local tests pass (`pytest`)
- [ ] Code formatted and linted (`ruff check .` / `black .`)

### 3. Documentation
- [ ] Code is documented with clear docstrings and comments where appropriate
- [ ] Relevant documentation in `docs/` or `README.md` has been updated

### 4. Data Privacy, Secrets & Model Weights Check
- [ ] **No secrets, API keys, or credentials** committed (check `.env` is NOT tracked)
- [ ] **No private audio recordings or unapproved raw datasets** committed
- [ ] **No heavy model checkpoints / weights** committed to Git (use designated artifact storage)
- [ ] Ran `git status` / `git diff --cached` to verify no accidental binary files are staged
