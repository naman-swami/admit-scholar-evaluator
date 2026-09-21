# Admit Scholar Holistic Admissions & Endowment Evaluator

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![EdTech](https://img.shields.io/badge/Domain-Higher_Education_Admissions-darkgreen.svg)](docs/holistic_admissions_framework.md)
[![Standard](https://img.shields.io/badge/Model-Holistic_Review_Index-teal.svg)](docs/holistic_admissions_framework.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

A university holistic admissions and endowment scholarship allocation platform balancing standardized academic indices with socioeconomic resilience indicators.

```
                    ┌─────────────────────────┐
                    │ Student Application Data│
                    │ (GPA, SAT, Income, Pubs)│
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ evaluators/scholarship  │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  Academic Index     │         │ Resilience Bonus    │
      │  (GPA + SAT Score)  │         │ (First-Gen & Need)  │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Admissions & Grant Plan │
                    │ (ADMIT_FELLOW / Grant $)│
                    └─────────────────────────┘
```

## Features

- **Holistic Scoring Matrix**: Synthesizes GPA, standardized testing, and research contributions.
- **Endowment Grant Optimization**: Automatically pairs high-resilience applicants with scholarship grants.
- **Applicant Cohort Benchmarks**: Includes multi-demographic student application records.

## Directory Structure

```
admit-scholar-evaluator/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint higher education provenance
├── evaluators/
│   └── scholarship_matrix.py        # Holistic scoring and endowment engine
├── fixtures/
│   └── applications/
│       └── sample_admissions_cohort.json # Benchmark applicant cohort
├── docs/
│   └── holistic_admissions_framework.md # Holistic admissions reference
├── tests/
│   └── test_agent.py                # Admissions test suite
├── admit.py                          # Admissions CLI
└── requirements.txt
```

## Quick Start

```bash
# Run admissions test suite
pytest tests/ -v

# Evaluate benchmark applicant cohort
python admit.py --demo
```
