from fastapi import FastAPI

from backend.schemas import StudentInput
from Graph.workflow import graph


app = FastAPI(
    title="Student Mental Health AI"
)


@app.get("/")
def home():
    return {
        "message": "Student Mental Health AI API"
    }


@app.post("/predict")
def predict(data: StudentInput):

    initial_state = {
        "age": data.age,
        "gender": data.gender,
        "country": data.country,
        "academic_level": data.academic_level,
        "most_used_platform": data.most_used_platform,
        "purpose_of_use": data.purpose_of_use,
        "avg_daily_usage_hours": data.avg_daily_usage_hours,
        "daily_unlocks": data.daily_unlocks,
        "study_hours": data.study_hours,
        "physical_activity_hours": data.physical_activity_hours,
        "sleep_hours_per_night": data.sleep_hours_per_night,
        "stress_level": data.stress_level
    }

    result = graph.invoke(initial_state)

    return {
        "mental_health_score": result["mental_health_score"],
        "risk_category": result["risk_category"],
        "ai_response": result["ai_response"]
    }


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)