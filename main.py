import json
import argparse
from src.admissions_engine import ScholarAdmissionsEngine

def main():
    parser = argparse.ArgumentParser(description="Scholar Admissions Evaluator CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated graduate fellowship dossier audit")
    args = parser.parse_args()

    engine = ScholarAdmissionsEngine()
    report = engine.evaluate_dossier(raw_grade=8.85, scale_type="10_point", publication_count=2, recommendation_score_5=4.8)
    print("="*60)
    print(" SCHOLARADMIT ACADEMIC MERIT & EQUITY AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
