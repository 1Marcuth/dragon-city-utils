from pydantic import validate_arguments

from .config import (
    damage_variant,
    attack_categories_powers,
    rank_class_powers,
    star_power
)

@validate_arguments
def calculate_attack_damage(
    category: int,
    level: int,
    attack_power: int,
    rank_class: int = 0,
    stars: int = 0,
) -> dict:
    initial_damage = attack_categories_powers[category]

    if rank_class > 0:
        rank_class_bonus = rank_class_powers[rank_class]
    
    else:
        rank_class_bonus = 0

    if stars > 0:
        star_bonus = star_power * stars

    else:
        star_bonus = 0

    damage = (1.5) * (1 + rank_class_bonus + star_bonus) * (initial_damage * (level ** 1.5 + 10) / 250) + attack_power

    minimum = round(damage_variant[0] * damage)
    maximum = round(damage_variant[1] * damage)
    average = round((minimum + maximum) / 2)

    return dict(
        minimum = minimum,
        maximum = maximum,
        average = average
    )

__all__ = [ calculate_attack_damage ]