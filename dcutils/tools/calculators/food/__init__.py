from pydantic import validate_call

from .config import feed_costs

@validate_call
def calculate_feed_cost(
    start_level: int,
    end_level: int
) -> int:
    cost = 0

    for i in range(start_level, end_level):
        cost += feed_costs[i]["total"]

    return cost