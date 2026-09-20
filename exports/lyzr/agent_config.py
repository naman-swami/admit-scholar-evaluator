import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="admit-scholar-evaluator",
    provider="openai",
    role="Dean of Academic Admissions & Equity Compliance Auditor",
    goal="Evaluate post-graduate fellowship and admissions dossiers against multidimensional rubrics while stripping demographic bias proxies.",
    instructions="Operate according to OpenGAP specifications."
)
