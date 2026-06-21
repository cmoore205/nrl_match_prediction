import numpy as np
import pytest
from sklearn.linear_model import LogisticRegression
from nrl.core.elo import expected_score

pytestmark = pytest.mark.unit

HOME_ADVANTAGE = 60.0
MEAN_ELO = 1500.0
ELO_SPREAD = 80.0

def _synthetic(n_matches: int, seed: int):
    """
    Creates synthethic matches where outcome depends on ELO + home edge.

    Input:
        n_matches: The amount of matches to generate.
        seed: A specific number to intialise sklearn's pseudo-random number generator. A specific seed
              should ensure the exact same results when running. 
    """
    random_seed = np.random.default_rng(seed)
    home_elo = random_seed.normal(MEAN_ELO, ELO_SPREAD, n_matches)
    away_elo = random_seed.normal(MEAN_ELO, ELO_SPREAD, n_matches)
    p_home = expected_score(home_elo, away_elo, home_advantage=HOME_ADVANTAGE)
    y = (random_seed.random(n_matches) < p_home).astype(int)
    X = (home_elo - away_elo).reshape(-1, 1)
    return X, y

def test_model_beats_always_home_baseline():
    train_size, test_size = 800, 400
    train_seed, test_seed = 42, 142

    X_train, y_train = _synthetic (train_size, train_seed)
    X_test, y_test = _synthetic(test_size, test_seed)

    model = LogisticRegression().fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    always_home = (y_test == 1).mean() ## this is a naive assumption that home always wins
    assert accuracy > always_home