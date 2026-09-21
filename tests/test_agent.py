import os
import pytest
from evaluators.scholarship_matrix import HolisticAdmissionsEngine

def test_presidential_fellow():
    res = HolisticAdmissionsEngine.evaluate_applicant(gpa=4.0, sat=1600, first_gen=True, family_income=40000.0, research_pubs=1)
    assert res["admissions_decision"] == "ADMIT_PRESIDENTIAL_FELLOW"
    assert res["scholarship_grant_usd"] == 45000.0
