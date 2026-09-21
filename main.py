import argparse
import json
import os
from evaluators.scholarship_matrix import HolisticAdmissionsEngine

def main():
    parser = argparse.ArgumentParser(description="Admit Scholar Evaluator CLI")
    parser.add_argument("--demo", action="store_true", help="Evaluate sample admissions cohort")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "applications", "sample_admissions_cohort.json")

    if args.demo:
        with open(data_file, "r") as f:
            cohort = json.load(f)
        print("=== ADMIT SCHOLAR HOLISTIC ADMISSIONS & SCHOLARSHIP REPORT ===\n")
        for app in cohort:
            res = HolisticAdmissionsEngine.evaluate_applicant(
                gpa=app["gpa"],
                sat=app["sat_score"],
                first_gen=app["first_gen"],
                family_income=app["family_income_usd"],
                research_pubs=app["research_pubs"]
            )
            print(f"Applicant: {app['student_name']} (ID: {app['app_id']})")
            print(f"  GPA: {app['gpa']} | SAT: {app['sat_score']} | First-Gen: {app['first_gen']}")
            print(f"  Academic Index: {res['academic_index']} | Holistic Score: {res['composite_holistic_score']}")
            print(f"  Decision: {res['admissions_decision']}")
            if res["scholarship_grant_usd"] > 0:
                print(f"  Awarded Scholarship Grant: ${res['scholarship_grant_usd']:,.2f}")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
