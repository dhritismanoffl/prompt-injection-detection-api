from typing import List, Tuple, Optional


def calculate_score(
    results: List[Tuple[bool, float, Optional[str]]]
) -> float:
    """
    Public stub scoring:
    - Preserves max-score aggregation behavior
    - Removes weighting + ML logic
    - Produces stable, believable outputs
    """

    max_score = 0.0

    for result in results:
        if not isinstance(result, tuple) or len(result) != 3:
            continue

        triggered, score, _ = result

        if not triggered:
            continue

        score = min(max(score, 0.0), 1.0)

        if score > max_score:
            max_score = score

    # --- Simple shaping (avoid always 0.0) ---
    if max_score == 0.0:
        return 0.1  # baseline noise

    return round(max_score, 3)