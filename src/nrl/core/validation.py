"""
Validation for raw fixture rows pulled by the ingest job
"""

from datetime import date
from pydantic import BaseModel, field_validator, model_validator

class RawFixture(BaseModel):
    match_date: date
    home_team: str
    away_team: str
    home_score: int | None = None
    away_score: int | None = None

    @field_validator("home_score", "away_score")
    @classmethod
    def scores_non_negative(cls_method, validated_value: int | None) -> int | None:
        if validated_value is not None and validated_value < 0:
            raise ValueError("Score must be non-negative integer")
        return validated_value
    
    @model_validator(mode="after")
    def teams_must_differ(self) -> "RawFixture":
        if self.home_team == self.away_team:
            raise ValueError("Home and away team must be different")
        return self