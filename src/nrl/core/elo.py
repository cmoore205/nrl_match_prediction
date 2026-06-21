"""
ELO Ratings. Shared by the training jobs and the serving API. 
"""

ELO_SCALE_FACTOR = 400.0
ELO_BASE = 10.0

def expected_score(rating_a: float, rating_b: float, home_advantage: float = 0.0) -> float:
    """
    Calculates probability that Team A beats Team B. 'home_advantage' gets added to Team A's rating.
    
    Input:
        rating_a: Team A's ELO (home team).
        rating_b: Team B's ELO (away team).
        home_advantage: Additional ELO given to the home team to account for the home field advantage.
    Returns:
        Probability that Team A beats Team B. 
    """
    return 1.0 / (1.0 + ELO_BASE ** ((rating_b - (rating_a + home_advantage)) / ELO_SCALE_FACTOR))

def update_ratings(
        rating_a: float,
        rating_b: float,
        result: float,
        k: float = 32.0,
        home_advantage: float = 0.0
) -> tuple[float, float]:
    """
    Updates each team's ELO based on the result of the game.

    Input:
        rating_a: Team A's ELO (home team).
        rating_b: Team B's ELO (away team).
        result: The actual outcome from Team A's perspective. 1.0 if Team A won, 0.0 if A lost, 0.5 for a draw. 
        k: K-factor. Controls how much ratings move per game, bigger means ratings react faster to each result.
        home_advantage: Additional ELO given to the home team to account for the home field advantage.

    Returns:
        A tuple of floats based on the outcome of the game played: (Team A New ELO, Team B New ELO) 
    """
    expected_outcome = expected_score(rating_a, rating_b, home_advantage)
    new_a = rating_a + k * (result - expected_outcome)
    new_b = rating_b + k * ((1.0 - result) - (1.0 - expected_outcome))
    return new_a, new_b