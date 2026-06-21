import pytest
from nrl.core.elo import expected_score, update_ratings

## Applying the unit marker to every test in that file at once
pytestmark = pytest.mark.unit

def test_equal_ratings_expected_is_half():
    assert expected_score(1500, 1500) == 0.5

def test_home_advantage_favours_home():
    assert expected_score(1500, 1500, home_advantage=65) > 0.5

def test_equal_ratings_win_shifts_by_half_k():
    ## The default K = 32. Equal ratings: winner gains 32 * (1 - 0.5) = 16
    new_home, new_away = update_ratings(1500, 1500, result=1.0)
    assert new_home == 1516.0
    assert new_away == 1484.0    

def test_draw_between_equals_leavings_ratings_unchanged():
    assert update_ratings(1500, 1500, result=0.5) == (1500.0, 1500.0)


def test_ratings_are_zero_sum():
    ## Whatever one team gains, the other must lose.
    new_home, new_away = update_ratings(1600, 1400, result=1.0, k=32)
    assert new_home == pytest.approx(1607.69, abs=0.01)
    assert new_away == pytest.approx(1392.31, abs=0.01)