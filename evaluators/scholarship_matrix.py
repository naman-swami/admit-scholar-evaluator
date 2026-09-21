"""
Admit Scholar Holistic Admissions & Endowment Allocation Engine
Evaluates academic index, socioeconomic resilience adversity, and merit/need scholarship grants.
"""
from typing import Dict, Any

class HolisticAdmissionsEngine:
    @staticmethod
    def evaluate_applicant(
        gpa: float,
        sat: int,
        first_gen: bool,
        family_income: float,
        research_pubs: int
    ) -> Dict[str, Any]:
        # Academic Index (0 - 100)
        gpa_score = (gpa / 4.0) * 50.0
        sat_score = (sat / 1600.0) * 50.0
        academic_index = round(gpa_score + sat_score, 1)

        # Adversity & Resilience Bonus (up to 15 points)
        adversity_bonus = 0.0
        if first_gen:
            adversity_bonus += 8.0
        if family_income < 65000.0:
            adversity_bonus += 7.0

        research_bonus = min(10.0, research_pubs * 5.0)

        composite = round(academic_index + adversity_bonus + research_bonus, 1)

        # Scholarship Grant Allocation
        scholarship_grant_usd = 0.0
        if composite >= 95.0:
            decision = "ADMIT_PRESIDENTIAL_FELLOW"
            scholarship_grant_usd = 45000.0
        elif composite >= 85.0:
            decision = "ADMIT_MERIT_HONORS"
            scholarship_grant_usd = 25000.0
        elif composite >= 75.0:
            decision = "ADMIT_REGULAR"
            scholarship_grant_usd = 10000.0 if family_income < 65000.0 else 0.0
        else:
            decision = "WAITLIST"

        return {
            "academic_index": academic_index,
            "composite_holistic_score": composite,
            "admissions_decision": decision,
            "scholarship_grant_usd": scholarship_grant_usd
        }
