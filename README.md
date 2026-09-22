# Admit Scholar Admissions & Fellowship Evaluator

> **Holistic University Admissions Review & Need-Aware Fellowship Allocation Engine**  
> Operationalizing Academic Indices, Contextual Resilience Bonuses, and Endowment Grants.

---

### Holistic Review Index Formulation

The composite evaluation index balances academic trajectory with contextual socioeconomic adversity:

$$\text{Composite Index} = 0.50 \cdot \text{AI}_{\text{norm}} + 0.30 \cdot \text{Curricular Rigor} + 0.20 \cdot \text{Contextual Resilience}$$

Where:
- $\text{AI}_{\text{norm}}$: Standardized GPA and percentile test rankings.
- **Contextual Resilience**: Multiplier derived from first-generation status, secondary school poverty index, and personal barriers overcome.

---

### Endowment Fellowship Matrix

```
                          Applicant Admitted
                                  │
                  ┌───────────────┴───────────────┐
                  ▼                               ▼
       Composite Index >= 92            Demonstrated Need >= $40k
                  │                               │
                  ▼                               ▼
      [Presidential Merit Scholar]     [Opportunity Grant Fellowship]
       $25,000 / year                   Full Tuition Endowment
```

---

### Admissions Operations CLI

```bash
# Evaluate benchmark university applicant cohort
python admit.py --demo

# Execute admissions algorithm unit tests
pytest tests/ -v
```

Endowment grant bylaws, financial need verification protocols, and academic index calculations are maintained in [ENDOWMENT_CRITERIA.md](ENDOWMENT_CRITERIA.md).
