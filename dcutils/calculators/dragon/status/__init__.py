from pydantic import validate_arguments

from .config import (
    dragon_rarity_power,
    level_and_category_power,
    damage_rune_power,
    hp_rune_power,
    rank_class_power,
    hp_tower_power,
    damage_tower_power
)

@validate_arguments
def calculate_status(
    category: int,
    rarity: str,
    level: int = 1,
    rank_class: int = 0,
    stars: int = 0,
    hp_runes: int = 0,
    damage_runes: int = 0,
    with_tower_bonus: bool = False
) -> dict:
    initial_status = level_and_category_power[category][level]
    initial_hp = initial_status["hp"]
    initial_damage = initial_status["damage"]

    hp = int(initial_hp)
    damage = int(initial_damage)

    if rank_class > 0:
        rank_class_factor = rank_class_power[rank_class] / 100

        rank_class_hp_bonus = initial_hp * rank_class_factor
        rank_class_damage_bonus = initial_damage * rank_class_factor

    else:
        rank_class_hp_bonus = 0
        rank_class_damage_bonus = 0

    if stars > 0:
        stars_factor = dragon_rarity_power[rarity][stars] / 100
        stars_hp_bonus = initial_hp * stars_factor
        stars_damage_bonus = initial_damage * stars_factor

    else:
        stars_hp_bonus = 0
        stars_damage_bonus = 0

    if hp_runes > 0:
        runes_hp_bonus = initial_hp * (hp_rune_power * hp_runes)
    
    else:
        runes_hp_bonus = 0
    
    if damage_runes > 0:
        runes_damage_bonus = initial_damage * (damage_rune_power * damage_runes)

    else:
        runes_damage_bonus = 0

    if with_tower_bonus:
        tower_hp_bonus = (stars_hp_bonus + runes_hp_bonus + rank_class_hp_bonus) * hp_tower_power
        tower_damage_bonus = (rank_class_damage_bonus + stars_damage_bonus + runes_damage_bonus) * damage_tower_power

    else:
        tower_hp_bonus = 0
        tower_damage_bonus = 0
    
    hp += stars_hp_bonus + runes_hp_bonus + rank_class_hp_bonus + tower_hp_bonus
    damage += rank_class_damage_bonus + stars_damage_bonus + runes_damage_bonus + tower_damage_bonus

    if category == 9:
        hp += hp * .10293

    hp = round(hp)
    damage = round(damage)

    return dict(
        result = dict(
            hp = hp,
            damage = damage
        ),
        initial = dict(
            hp = initial_hp,
            damage = initial_damage, 
        ),
        bonus = dict(
            rank_class = dict(
                hp = round(rank_class_hp_bonus),
                damage = round(rank_class_damage_bonus)
            ),
            stars = dict(
                hp = round(stars_hp_bonus),
                damage = round(stars_damage_bonus)
            ),
            runes = dict(
                hp = round(runes_hp_bonus),
                damage = round(runes_damage_bonus)
            ),
            tower = dict(
                hp = round(tower_hp_bonus),
                damage = round(tower_damage_bonus)
            )
        )
    )

__all__ = [ calculate_status ]