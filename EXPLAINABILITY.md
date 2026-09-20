# Explainability — admit-scholar-evaluator

## Decision Reasoning
ScholarAdmit deconstructs candidate dossiers into objective competency vectors, evaluating coursework difficulty and scientific contribution independently of demographic markers.

## Data Sources and Inputs Used
AACRAO Edge international credential database, NSF graduate fellowship rubrics, publication citation metrics, and Title VI equity guidelines.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, admit-scholar-evaluator assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, admit-scholar-evaluator will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, admit-scholar-evaluator explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
admit-scholar-evaluator actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Final Admissions Decisions: All acceptance/rejection decisions are made exclusively by human faculty committees.
- Credential Verification: Does not verify physical university seal authenticity or investigate diploma mill fraud directly.
- In-Person Interviews: Does not evaluate personal presence or live non-verbal body language.
- Institutional Quotas: Does not enforce arbitrary institutional demographic quotas.

## Uncertainty Quantification Approach
When international grading scales lack standardized conversion documentation, ScholarAdmit flags the dossier for manual credential evaluation specialist review.
