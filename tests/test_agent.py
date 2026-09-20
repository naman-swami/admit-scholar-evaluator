import pytest
from src.admissions_engine import ScholarAdmissionsEngine

def test_gpa_normalization():
    engine = ScholarAdmissionsEngine()
    assert engine.normalize_gpa(9.0, "10_point") == 3.60
    assert engine.normalize_gpa(18.0, "20_point_french") == 3.60

def test_fellowship_admission():
    engine = ScholarAdmissionsEngine()
    res = engine.evaluate_dossier(9.5, "10_point", publication_count=3, recommendation_score_5=5.0)
    assert res["admissions_recommendation"] == "FELLOWSHIP_NOMINEE"
