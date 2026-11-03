# Contribution & Collaboration Guidelines

Welcome to the team! To maintain high code quality, reproducibility, and data privacy across our final-year project, please follow these guidelines carefully.

---

## 1. Golden Rule: No Direct Commits to `main`
- The `main` branch is **protected** and represents production-ready, stable, and peer-reviewed code.
- **Direct commits or pushes to `main` are strictly forbidden.**
- All code changes must be submitted via feature/fix branches and merged through GitHub **Pull Requests (PRs)** with at least one team member's approval.

---

## 2. Branch Naming Conventions
Always create a branch from the latest `main`:
```bash
git checkout main
git pull origin main
git checkout -b <branch-type>/<issue-id>-<short-description>
```

### Branch Types:
| Type | Purpose | Example |
| :--- | :--- | :--- |
| `feat/` | New functionality or module | `feat/FYP-12-audio-dataloader` |
| `fix/` | Bug fixes | `fix/FYP-34-sampling-rate-mismatch` |
| `docs/` | Documentation improvements | `docs/FYP-05-update-readme` |
| `refactor/` | Code refactoring without changing behavior | `refactor/FYP-20-modularize-models` |
| `test/` | Adding or updating unit tests | `test/FYP-15-eval-harness-tests` |
| `chore/` | Build scripts, dependencies, configs | `chore/FYP-02-setup-pyproject` |

---

## 3. Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<OWNER>/<REPO>.git
   cd FinalYear
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install development dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements-dev.txt
   # OR with editable pyproject installation:
   pip install -e ".[dev]"
   ```

4. **Setup environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your local credentials if needed
   ```

---

## 4. Commit Message Standard
Write descriptive, imperative commit messages:
- `feat(data): add audio preprocessing script with 16kHz resampler`
- `fix(eval): correct metric computation for WER`
- `docs(setup): add virtual environment troubleshooting guide`

---

## 5. Pull Request Process & Review Workflow

1. **Keep branches synchronized:**
   Before pushing, ensure your branch is up-to-date with `main`:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Run tests & linters locally:**
   ```bash
   pytest
   ruff check .
   ```

3. **Push your branch to GitHub:**
   ```bash
   git push -u origin <branch-type>/<issue-id>-<short-description>
   ```

4. **Open a Pull Request:**
   - Base branch: `main`
   - Compare branch: `your-branch`
   - Fill in the PR template completely:
     - Link your **Jira Ticket**
     - Summarize what changed and why
     - Confirm all PR checklist items (tests, docs, privacy/secrets)

5. **Code Review:**
   - Request review from your peer (e.g. Person A / Project Partner).
   - Address any reviewer feedback or questions.
   - Once approved and CI checks pass, merge using **Squash and Merge** or **Rebase and Merge**.

---

## 6. Privacy, Security & Artifact Rules

> [!CAUTION]
> **Strictly check your commits before pushing!**
> - **Never commit secrets:** API keys, tokens, `.env` files, or passwords.
> - **Never commit raw/private audio files:** Keep audio files in `data/raw/` (ignored by `.gitignore`).
> - **Never commit unapproved datasets:** Check data licensing and ethics before storage.
> - **Never commit large model weights:** Store `.pt`, `.safetensors`, `.bin` in shared cloud storage or artifact buckets.

### Self-Audit Command:
Before pushing, run:
```bash
git status
git diff --cached --stat
```
Ensure no `.env`, `.wav`, `.mp3`, `.pt`, or dataset files appear in the staged list.
