from pydantic import validate_arguments

from .config import (
    category_9_dragons_hp_fix,
    dragon_rarity_power,
    category_and_level_power,
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
    with_tower_bonus: bool = False,
    extra_hp_multiplier: float = 0.0,
    extra_damage_multiplier: float = 0.0
) -> dict:
    initial_status = category_and_level_power[category][level]
    initial_hp = initial_status["hp"]
    initial_damage = initial_status["damage"]

    hp = float(initial_hp)
    damage = float(initial_damage)

    rank_class_hp_bonus = 0
    rank_class_damage_bonus = 0
    stars_hp_bonus = 0
    stars_damage_bonus = 0
    runes_hp_bonus = 0
    runes_damage_bonus = 0
    tower_hp_bonus = 0
    tower_damage_bonus = 0
    extra_hp_bonus = 0
    extra_damage_bonus = 0

    if rank_class > 0:
        rank_class_factor = rank_class_power[rank_class] / 100
        rank_class_hp_bonus = initial_hp * rank_class_factor
        rank_class_damage_bonus = initial_damage * rank_class_factor

    if stars > 0:
        stars_factor = dragon_rarity_power[rarity][stars] / 100
        stars_hp_bonus = initial_hp * stars_factor
        stars_damage_bonus = initial_damage * stars_factor

    if hp_runes > 0:
        runes_hp_bonus = initial_hp * (hp_rune_power * hp_runes)
    
    if damage_runes > 0:
        runes_damage_bonus = initial_damage * (damage_rune_power * damage_runes)

    if with_tower_bonus:
        tower_hp_bonus = (hp + (stars_hp_bonus + runes_hp_bonus + rank_class_hp_bonus)) * hp_tower_power
        tower_damage_bonus = (damage + (rank_class_damage_bonus + stars_damage_bonus + runes_damage_bonus)) * damage_tower_power

    if extra_hp_multiplier > 0.0:
        extra_hp_bonus = (hp + (stars_hp_bonus + runes_hp_bonus + rank_class_hp_bonus)) * extra_hp_multiplier

    if extra_damage_multiplier > 0.0:
        extra_damage_bonus = (damage + (stars_damage_bonus + runes_damage_bonus + rank_class_damage_bonus)) * extra_damage_multiplier

    hp += stars_hp_bonus + runes_hp_bonus + rank_class_hp_bonus + tower_hp_bonus + extra_hp_bonus
    damage += rank_class_damage_bonus + stars_damage_bonus + runes_damage_bonus + tower_damage_bonus + extra_damage_bonus

    if category == 9:
        hp += hp * category_9_dragons_hp_fix

    hp = round(hp)
    damage = round(damage)

    return dict(
        result = dict(
            hp = hp,
            damage = damage
        ),
        initial = dict(
            hp = round(initial_hp if category != 9 else initial_hp * (category_9_dragons_hp_fix + 1)),
            damage = round(initial_damage), 
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
            ),
            extra = dict(
                hp = round(extra_hp_bonus),
                damage = round(extra_damage_bonus)
            )
        )
    )

__all__ = [ "calculate_status" ]