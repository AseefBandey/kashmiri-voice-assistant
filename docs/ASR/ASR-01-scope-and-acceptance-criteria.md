# ASR-01: Define ASR Scope and Acceptance Criteria

**Project:** Kashmiri Voice AI  
**Task ID:** ASR-01  
**Assigned To:** Person A  
**Priority:** High  
**Deadline:** End of Week 1  
**Status:** Scope Finalized

---

## 1. Objective

The objective of this task is to define the scope, functionality, technical requirements, and acceptance criteria for the Automatic Speech Recognition (ASR) component of the Kashmiri Voice AI project.

The ASR component will convert spoken Kashmiri language into written Kashmiri text using the Perso-Arabic script.

The resulting text will serve as input for downstream NLP or Large Language Model (LLM) components.

## 2. Finalized Project Decisions

| Parameter          | Final Decision                                   |
| ------------------ | ------------------------------------------------ |
| Target Language    | Kashmiri                                         |
| Writing Script     | Perso-Arabic                                     |
| Audio Input        | Recorded audio                                   |
| Audio Format       | WAV (initial support)                            |
| Sample Rate        | 16 kHz (target processing rate)                  |
| Dialect Coverage   | Multiple regional Kashmiri varieties             |
| Model Strategy     | Comparative evaluation                           |
| Approaches         | Pretrained fine-tuning and training from scratch |
| Primary Objective  | Balance accuracy and computational cost          |
| Initial Deployment | Local inference                                  |
| Output             | Transcribed Kashmiri text                        |

## 3. Functional Scope (V1)

The ASR system will perform the following operations:

1. Accept recorded Kashmiri audio as input.
2. Preprocess audio through resampling, normalization and basic noise handling.
3. Extract speech features or process audio directly using the selected model.
4. Recognize spoken Kashmiri words.
5. Generate written Kashmiri text in Perso-Arabic script.
6. Return the transcription in a format that can be passed to downstream NLP/LLM components.

### System Workflow

Recorded Kashmiri Audio  
↓  
Audio Preprocessing  
↓  
Speech Recognition Model  
↓  
Text Decoding  
↓  
Kashmiri Text (Perso-Arabic)  
↓  
Downstream NLP / LLM

## 4. Features Outside V1 Scope

The following features are excluded from the initial implementation:

- Real-time microphone transcription.
- Automatic translation into English.
- Speaker identification and diarization.
- Text-to-Speech generation.
- Conversational response generation.
- Mobile application deployment.
- Automatic conversion between different Kashmiri writing scripts.

These features may be considered in future development phases.

## 5. Dataset Requirements

The dataset should contain recorded Kashmiri speech paired with accurate human-verified transcripts.

The dataset collection strategy should consider:

- Multiple regional Kashmiri dialects.
- Male and female speakers.
- Different age groups where feasible.
- Different speaking speeds and speaking styles.
- Short sentences and longer conversational speech.
- Clean recordings and recordings with moderate background noise.

### Dataset Structure

Each audio sample should have a corresponding transcript and metadata.

Suggested metadata fields:

| Field       | Description                             |
| ----------- | --------------------------------------- |
| audio_id    | Unique recording identifier             |
| audio_path  | Audio file location                     |
| transcript  | Verified Kashmiri transcription         |
| speaker_id  | Anonymous speaker identifier            |
| dialect     | Regional variety                        |
| gender      | Speaker gender, if voluntarily provided |
| duration    | Recording duration                      |
| sample_rate | Audio sample rate                       |

The dataset must be divided into training, validation and independent testing sets.

**Important:** Recordings from the same speaker should not be randomly distributed across all three sets. Speaker-independent evaluation will help measure generalization to previously unseen speakers.

## 6. Model Development Strategy

Two approaches will be investigated.

### Approach A: Pretrained Multilingual Model

- Identify existing multilingual speech recognition models.
- Evaluate their existing support for Kashmiri.
- Fine-tune suitable models using Kashmiri speech datasets.
- Measure accuracy, inference speed and resource consumption.

### Approach B: Model Training from Scratch

- Investigate suitable ASR architectures.
- Design a model training pipeline.
- Train using the collected Kashmiri speech dataset.
- Evaluate computational requirements and recognition performance.

### Comparative Evaluation

Both approaches will be compared based on:

1. Word Error Rate (WER).
2. Character Error Rate (CER).
3. Training time.
4. Inference latency.
5. Memory requirements.
6. Hardware requirements.
7. Generalization across regional dialects.

The final approach will be selected based on the balance between transcription quality and computational feasibility.

Training from scratch will be considered a research comparison, subject to sufficient training data and hardware availability.

## 7. Acceptance Criteria

The following are initial engineering targets for ASR V1, not guaranteed performance results.

| Evaluation Parameter   | Target                                                |
| ---------------------- | ----------------------------------------------------- |
| Language Recognition   | Kashmiri                                              |
| Output Script          | Perso-Arabic                                          |
| Audio Input            | WAV                                                   |
| Processing Sample Rate | 16 kHz                                                |
| Character Error Rate   | ≤ 15%                                                 |
| Word Error Rate        | ≤ 25%                                                 |
| Dialect Support        | Multiple regional varieties represented in evaluation |
| Execution              | Local inference                                       |
| Output                 | Machine-readable Kashmiri transcription               |

The CER and WER targets will be evaluated on an independent test dataset.

If the targets cannot be achieved, actual performance must be documented with error analysis and recommendations for improvement rather than reporting the system as successful without evidence.

## 8. Evaluation Metrics

### Word Error Rate (WER)

WER measures the difference between the predicted transcription and the reference transcription at the word level.

WER = (S + D + I) / N

Where:

- S = Substitutions
- D = Deletions
- I = Insertions
- N = Number of words in the reference transcript.

### Character Error Rate (CER)

CER measures transcription errors at the character level.

CER = (S + D + I) / N

Here, all calculations are performed at the character level.

Both metrics will be used because character-level evaluation can provide additional insight into spelling errors and transcription quality.

A consistent text normalization policy must be established before evaluation, including Unicode normalization, punctuation handling and word segmentation.

## 9. Testing Requirements

The system must be tested against:

- Previously unseen speakers.
- Different regional Kashmiri dialects.
- Different speaking speeds.
- Short and long speech recordings.
- Different recording conditions.
- Moderate background noise.

Performance should be reported overall and separately for each represented dialect where sufficient test data exists.

## 10. Deliverables

At the completion of ASR-01, the following deliverables must be available:

1. Finalized ASR scope document.
2. Functional and non-functional requirements.
3. Initial dataset requirements.
4. Defined evaluation metrics.
5. Model comparison strategy.
6. Acceptance criteria.
7. Initial ASR architecture workflow.

## 11. Definition of Done

- [x] Target language finalized.
- [x] Perso-Arabic script selected.
- [x] Recorded audio selected as initial input.
- [x] Multiple dialect coverage selected.
- [x] Comparative model strategy selected.
- [x] Accuracy and computational cost identified as primary objectives.
- [x] Initial evaluation targets defined.
- [ ] Dataset requirements reviewed and approved.
- [ ] Evaluation and normalization protocols finalized.
- [ ] Document added to the shared GitHub repository.

---

## 12. Expected Outcome

At the completion of ASR-01, the project team will have a clearly defined technical direction for developing the Kashmiri ASR system.

This document will act as the foundation for subsequent tasks involving existing model research, dataset identification, data preparation, model selection, training and evaluation.

**Next Task:** ASR-02 — Research Existing ASR Models and Architectures for Kashmiri and Multilingual Speech Recognition.
