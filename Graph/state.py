from typing import TypedDict


class StudentState(TypedDict, total=False):

    
    age: int

    gender: str

    country: str

    grouped_country: str

    academic_level: str

    most_used_platform: str

    purpose_of_use: str

    avg_daily_usage_hours: float

    daily_unlocks: int

    study_hours: float

    physical_activity_hours: float

    sleep_hours_per_night: float

    stress_level: str


    mental_health_score: float


    risk_category: str


    ai_response: str