# Kashmiri Voice Assistant

A speech processing project focused on building a reproducible Kashmiri voice assistant with automatic speech recognition (ASR), orthographic normalization, natural language processing, and text-to-speech capabilities.

---

## Overview

The **Kashmiri Voice Assistant** aims to enable natural voice-based interaction in Kashmiri through a modular speech processing pipeline. The project focuses on improving speech recognition accuracy, standardizing Kashmiri text representations, and supporting end-to-end spoken communication.

The ASR workstream focuses on developing and evaluating Kashmiri speech-to-text models through reproducible experiments and standardized evaluation metrics.

## Key Objectives

- **Acoustic Modeling:** Fine-tune multilingual speech recognition models on Kashmiri speech data.
- **Orthographic Normalization:** Standardize Kashmiri Perso-Arabic Unicode representations, character variants, and diacritics.
- **Model Evaluation:** Benchmark speech recognition performance using Word Error Rate (WER) and Character Error Rate (CER).
- **Conversational Processing:** Integrate recognized speech with NLP and language model components.
- **Speech Synthesis:** Generate spoken Kashmiri responses through text-to-speech (TTS).

## Project Architecture

The system follows a modular pipeline that transforms spoken Kashmiri input into an intelligible spoken response.

```mermaid
flowchart LR
    A["Kashmiri Voice Input"] --> B["Audio Processing"]
    B --> C["Kashmiri ASR<br/>Speech-to-Text"]
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

## Repository Structure

```text
kashmiri-voice-assistant/
├── README.md
├── .gitignore
├── .env.example
├── pyproject.toml          # Project configuration and dependencies
├── docs/                  # Documentation
├── configs/               # Model and experiment configurations
├── data/                  # Local or approved datasets (not tracked)
├── notebooks/              # Research and experimentation notebooks
├── src/
│   └── voice_assistant/
│       └── asr/           # Speech recognition and normalization
├── scripts/               # Training, evaluation, and utility scripts
├── reports/               # Evaluation results and experiment reports
└── tests/                 # Automated tests
```

## Getting Started

### Prerequisites

- Python 3.10 or later
- Git
- A compatible environment for the selected speech recognition models

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AseefBandey/kashmiri-voice-assistant.git
   cd kashmiri-voice-assistant
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows:

   ```powershell
   .venv\Scripts\activate
   ```

3. Install the project and development dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -e ".[dev]"
   ```

4. Configure environment variables:

   ```bash
   cp .env.example .env
   ```

   Update `.env` with the required local configuration. Do not commit secrets or credentials.

## Testing

Run the automated test suite to verify the development environment and implemented components.

Using `unittest`:

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

Or, if `pytest` is configured:

```bash
pytest
```

## Evaluation

Speech recognition performance is evaluated using the following metrics:

| Metric | Description |
|---|---|
| Word Error Rate (WER) | Measures word-level transcription errors, including substitutions, deletions, and insertions. |
| Character Error Rate (CER) | Measures character-level transcription errors, including substitutions, deletions, and insertions. |

Evaluation should use consistent datasets, preprocessing procedures, and normalization rules to ensure meaningful comparisons between model configurations.

## Data and Reproducibility

- Use datasets that are publicly available, appropriately licensed, or otherwise approved for research.
- Keep raw audio and other large datasets out of version control.
- Document dataset sources, preprocessing steps, model configurations, and evaluation settings.
- Record experiment results and model versions to support reproducibility.

## Development Status

This repository supports the ongoing development of the Kashmiri speech recognition and voice assistant pipeline. Individual components may be under active development.

## Contributing

Contributions to speech recognition, text normalization, evaluation, documentation, and testing are welcome.

When contributing:

1. Keep changes modular and reproducible.
2. Add or update tests for new functionality.
3. Document relevant configuration and preprocessing changes.
4. Follow the existing project structure and coding conventions.

## License

A license has not yet been specified. Please check the repository for licensing information before using, modifying, or redistributing the project.

---

**Project:** Kashmiri Voice Assistant  

