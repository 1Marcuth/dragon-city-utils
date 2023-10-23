from pydantic import validate_call

from .config import (
    ORB_RECALL_CONFIG,
    DRAGON_MIN_LEVEL,
    DRAGON_MAX_LEVEL,
    DRAGON_MIN_STARS,
    DRAGON_MAX_STARS
)

@validate_call
def calculate_recall_gain(dragon_level: int, dragon_stars: int) -> int:
    orbs_gain = 0

    if dragon_level < DRAGON_MIN_LEVEL or dragon_level > DRAGON_MAX_LEVEL:
        raise ValueError(f"'{dragon_level}' is not a valid level for a dragon, choose a level between '{DRAGON_MIN_LEVEL}' and '{DRAGON_MAX_LEVEL}'")

    if dragon_stars < DRAGON_MIN_STARS or dragon_stars > DRAGON_MAX_STARS:
        raise ValueError(f"'{dragon_stars}' It is not a number of stars valid for a dragon, choose a number of stars between '{DRAGON_MIN_STARS}' and '{DRAGON_MAX_STARS}'")

    for i in range(dragon_level if dragon_level <= 30 else 30):
        orbs_gain += ORB_RECALL_CONFIG["per_levels"][i]

    for i in range(dragon_stars):
        orbs_gain += ORB_RECALL_CONFIG["per_stars"][i]

    return orbs_gain

__all__ = [ "calculate_recall_gain" ]