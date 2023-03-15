from pydantic import validate_arguments
import random

from .config import (
    damage_variant,
    attack_categories_power,
    rank_class_power,
    one_star_power
)

@validate_arguments
def calculate_attack_damage(
    category: int,
    level: int,
    attack_power: int,
    rank_class: int = 0,
    stars: int = 0
) -> dict:
    initial_damage = attack_categories_power[category]

    rank_class_bonus = 0
    stars_bonus = 0

    if rank_class > 0:
        rank_class_bonus = rank_class_power[rank_class]  

    if stars > 0:
        stars_bonus = one_star_power * stars
        
    damage = 1.5 * (1 + rank_class_bonus + stars_bonus) * (initial_damage * (level ** 1.5 + 10) / 250) + attack_power

    minimum = round(damage_variant[0] * damage)
    maximum = round(damage_variant[1] * damage)
    average = round((minimum + maximum) / 2)

    random_damage = round(
        random.randint(
            int(damage_variant[0] * 100),
            int(damage_variant[1] * 100)
        ) / 100
            *
        damage
    )

    return dict(
        minimum = minimum,
        maximum = maximum,
        average = average,
        random = random_damage
    )

__all__ = [ "calculate_attack_damage" ]