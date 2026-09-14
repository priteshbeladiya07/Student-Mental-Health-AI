from pydantic import BaseModel, Field


class StudentInput(BaseModel):

    age: int = Field(ge=10, le=100)

    gender: str
    country: str
    academic_level: str
    most_used_platform: str
    purpose_of_use: str

    avg_daily_usage_hours: float = Field(ge=0, le=24)
    daily_unlocks: int = Field(ge=0)

    study_hours: float = Field(ge=0, le=24)
    physical_activity_hours: float = Field(ge=0, le=24)
    sleep_hours_per_night: float = Field(ge=0, le=24)

    stress_level: str