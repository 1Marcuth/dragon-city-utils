from pydantic import validate_call

@validate_call
def calculate_feed_cost(
    start_level: int,
    end_level: int,
    dragon_rarity: str
) -> int:
    ...