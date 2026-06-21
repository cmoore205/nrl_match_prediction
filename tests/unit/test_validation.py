from datetime import date
import pytest
from pydantic import ValidationError
from nrl.core.validation import RawFixture

pytestmark = pytest.mark.unit

def test_valid_fixture_is_accepted():
    fixture = RawFixture(
        match_date=date(2026, 6, 20),
        home_team="Storm", away_team="Broncos",
        home_score=24, away_score=12
    )
    assert fixture.home_team == "Storm"

def test_negative_score_is_rejected():
    with pytest.raises(ValidationError):
        RawFixture(
            match_date=date(2026, 6, 20),
            home_team="Storm", away_team="Broncos",
            home_score=-10, away_score=20
        )

def test_same_team_twice_is_rejected():
    with pytest.raises(ValidationError):
        RawFixture(
            match_date=date(2026, 6, 20),
            home_team="Storm", away_team="Storm",
            home_score=20, away_score=10
        )

def test_missing_date_is_rejected():
    with pytest.raises(ValidationError):
        RawFixture(
            home_team="Storm", away_team="Broncos",
            home_score=20, away_score=10
        )