import joblib

from Graph.state import StudentState
from backend.llm.prompts import (
    SYSTEM_PROMPT,
    LOW_PROMPT,
    MODERATE_PROMPT,
    HIGH_PROMPT
)

from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import pandas as pd
load_dotenv()



model = joblib.load("backend/Mental_Health_Model.pkl")



llm = ChatMistralAI(
    model="codestral-2508",
    max_tokens=300,
    temperature=0.3
)


def ml_prediction(state: StudentState):

    data = pd.DataFrame([{
        "Study_Hours": state["study_hours"],
        "Age": state["age"],
        "Avg_Daily_Usage_Hours": state["avg_daily_usage_hours"],
        "Daily_Unlocks": state["daily_unlocks"],
        "Physical_Activity_Hours": state["physical_activity_hours"],
        "Sleep_Hours_Per_Night": state["sleep_hours_per_night"],
        "Stress_Level": state["stress_level"],
        "Gender": state["gender"],
        "Academic_Level": state["academic_level"],
        "Most_Used_Platform": state["most_used_platform"],
        "Purpose_Of_Use": state["purpose_of_use"],
        "Grouped_country": state["grouped_country"]
    }])

    score = model.predict(data)[0]

    return {
        "mental_health_score": round(float(score), 2)
    }

def classify_risk(state: StudentState):

    score = state["mental_health_score"]

    if score >= 7:
        risk = "LOW"

    elif score >= 5:
        risk = "MODERATE"

    else:
        risk = "HIGH"

    return {
        "risk_category": risk
    }

def generate_response(state: StudentState):

    risk = state["risk_category"]

    prompt_data = {
        "score": state["mental_health_score"],
        "age": state["age"],
        "academic_level": state["academic_level"],
        "platform": state["most_used_platform"],
        "purpose": state["purpose_of_use"],
        "usage": state["avg_daily_usage_hours"],
        "unlocks": state["daily_unlocks"],
        "study_hours": state["study_hours"],
        "activity": state["physical_activity_hours"],
        "sleep": state["sleep_hours_per_night"],
        "stress": state["stress_level"]
    }

    if risk == "LOW":
        prompt = LOW_PROMPT.format(**prompt_data)

    elif risk == "MODERATE":
        prompt = MODERATE_PROMPT.format(**prompt_data)

    else:
        prompt = HIGH_PROMPT.format(**prompt_data)

    response = llm.invoke([
        ("system", SYSTEM_PROMPT),
        ("human", prompt)
    ])

    return {
        "ai_response": response.content
    }

top_countries = [
    "India",
    "USA",
    "Canada",
    "Australia",
    "UK",
    "Germany",
    "Mexico",
    "Turkey",
    "France"
]

def group_country_node(state):
    country = state["country"]

    if country in top_countries:
        grouped_country = country
    else:
        grouped_country = "Other"

    return {
        "grouped_country": grouped_country
    }