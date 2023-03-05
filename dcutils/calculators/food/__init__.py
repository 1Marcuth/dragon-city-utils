from pydantic import validate_arguments

@validate_arguments
def calculate_feed_cost(
    start_level: int,
    end_level: int,
    dragon_rarity: str
) -> int:
    ...