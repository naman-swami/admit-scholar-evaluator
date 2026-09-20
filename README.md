# ScholarAdmit — Holistic Academic Admissions & Fellowship Dossier Evaluator

[![OpenGAP Compliant](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](https://opengap.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Ethical academic dossier evaluation assistant scoring holistic merit, curricular rigor, and research potential with proactive affirmative bias mitigation.

## Domain Category
**Other**

## Architecture
- **OpenGAP Specification**: `0.1.0`
- **Role**: Dean of Academic Admissions & Equity Compliance Auditor
- **Primary Goal**: Evaluate post-graduate fellowship and admissions dossiers against rigorous multidimensional rubrics while stripping demographic bias proxies.

## Skills Included
- **`transcript-rigor-normalizing`**: Normalizing grade point trends across diverse global grading scales and course difficulty indices.
- **`research-statement-appraisal`**: Extracting intellectual vitality, methodology maturity, and independent research contributions from candidate statements.
- **`adverse-impact-auditing`**: Conducting four-fifths rule and demographic parity checks across committee scoring distribution curves.

## Tools Schema
- **`normalize-academic-transcript`**: Convert international tertiary transcripts into standardized ECTS/US semester credit and GPA equivalencies.
- **`evaluate-recommendation-sentiment`**: Analyze letter of recommendation strength, faculty superlatives, and institutional context indicators.
- **`audit-committee-bias-distribution`**: Compute statistical divergence between evaluators to flag outlier scoring anomalies.

## Explainability & Verification
Full explainability compliance under OpenGAP Checkpoint 2 is detailed in [EXPLAINABILITY.md](EXPLAINABILITY.md), covering:
- Decision Reasoning
- Data Sources and Inputs Used
- Confidence Scoring Methodology
- Source Attribution Protocol
- Bias Awareness
- Limitation Taxonomy per Domain
- Uncertainty Quantification Approach

## Multi-Framework Compatibility
Adapters and visa export configurations are included in `exports/`:
- Anthropic Claude (`claude-system-prompt.txt`)
- OpenAI Assistants (`openai-assistant.json`)
- LangChain (`langchain-agent.json`)
- CrewAI (`crewai-agent.json`)
- AutoGen (`autogen-agent.json`)

## License
MIT License
