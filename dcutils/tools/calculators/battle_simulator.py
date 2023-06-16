from pydantic import validate_arguments
from pyfilter.tuple_list import FromTupleList
from rich import print
import random

from .dragon import calculate_attack_damage, calculate_status
from .elements import calculate_strongs, calculate_weaknesses

class SimulationTypes:
    NORMAL = 0

def select_best_attack(
    attacks: list[tuple[str, int]],
    enemy_weaknesses: list[str],
    enemy_main_element: str
) -> tuple[str, int]:
    selected_attack: tuple[str, int]
    attacks_with_strong = []
    enemy_strongs = calculate_strongs([ enemy_main_element ])

    for attack in attacks:
        attack_element = attack[0]

        for enemy_weakness in enemy_weaknesses:
            weakness_element = enemy_weakness[0]

            if weakness_element == attack_element:
                attacks_with_strong.append(attack)

    if len(attacks_with_strong) > 0:
        attacks_with_strongs_power_max = max([ attack[1] for attack in attacks_with_strong ])
        selected_attack = FromTupleList(attacks_with_strong).get_with_value(attacks_with_strongs_power_max)

    else:
        attacks_without_null = [
            attack for attack in attacks
            if attack[0] != enemy_main_element
        ]

        attacks_without_weaknesses = [
            attack for attack in attacks_without_null
            if attack[0] in enemy_strongs
        ]

        if len(attacks_without_weaknesses) > 0:
            attacks_without_weaknesses_power_max = max([ attack[1] for attack in attacks_without_weaknesses ])
            attack_without_weaknesses = FromTupleList(attacks_without_weaknesses).get_with_value(attacks_without_weaknesses_power_max)
            selected_attack = attack_without_weaknesses

        else:
            if len(attacks_without_null) > 0:
                attack_power_max = max([ attack[1] for attack in attacks_without_null ])
                attack = FromTupleList(attacks).get_with_value(attack_power_max)
                selected_attack = attack

            else:
                selected_attack = attacks[0]

    return selected_attack

class Entity:
    def __init__(
        self,
        category: int,
        level: int,
        rank_class: int,
        starts: int,
        hp: int,
        elements: list[str],
        attacks: list[tuple[str, int]]
    ) -> None:
        self.__category = category
        self.__level = level
        self.__rank_class = rank_class
        self.__stars = starts

        attack_elements = [ attack[0] for attack in attacks ]

        self.elements = elements
        self.main_element = elements[0]
        self.weaknesses = calculate_weaknesses(self.main_element)
        self.strongs = calculate_strongs(attack_elements)
        self.attacks = attacks
        self.current_hp = int(hp)

    @validate_arguments
    def attack(self, entity, attack: tuple[str, int]):
        attack_element, attack_power = attack

        damage = calculate_attack_damage(
            self.__category,
            self.__level,
            attack_power,
            self.__rank_class,
            self.__stars
        )["random"]

        is_strong_damage = False
        is_weak_damage = False
        
        attack_strongs = calculate_strongs([ attack_element ])
        attack_weaknesses = calculate_weaknesses(attack_element)
        dragon_main_element_strongs = calculate_strongs([ entity.main_element ])

        damage_type = "normal"

        for strong in attack_strongs:
            if strong in entity.weaknesses:
                is_strong_damage = True
                break

        for weakness in attack_weaknesses:
            if weakness in dragon_main_element_strongs:
                is_weak_damage = True
                break

        if is_strong_damage:
            damage += damage
            damage_type = "strong"
        
        elif is_weak_damage:
            damage -= int(damage / 2)
            damage_type = "weak"

        entity.take_damage(damage)

        return dict(
            damage = damage,
            damage_type = damage_type
        )

    @validate_arguments
    def take_damage(self, damage: int):
        self.current_hp -= damage

        if self.current_hp < 0:
            self.current_hp = 0

    @property
    def is_alive(self) -> bool:
        return self.current_hp > 0

@validate_arguments
def process_entity(
    category: int,
    rarity: str,
    level: int,
    rank_class: int,
    stars: int,
    hp_runes: int,
    damage_runes: int,
    with_tower_bonus: bool,
    extra_hp_multiplier: float,
    extra_damage_multiplier: float,
    elements: list[str],
    attacks: list[tuple[str, int]],
) -> Entity:
    status = calculate_status(
        category,
        rarity,
        level,
        rank_class,
        stars,
        hp_runes,
        damage_runes,
        with_tower_bonus,
        extra_hp_multiplier,
        extra_damage_multiplier,
    )

    hp = status["result"]["hp"]

    entity = Entity(
        category,
        level,
        rank_class,
        stars,
        hp,
        elements,
        attacks
    )

    return entity

class BattleSimulator:
    @validate_arguments
    def __init__(
        self,
        team1_data: list[dict],
        team2_data: list[dict]
    ) -> None:
        team1 = [ process_entity(**entity_data) for entity_data in team1_data ]
        team2 = [ process_entity(**entity_data) for entity_data in team2_data ]

        self.__teams = [team1, team2]
        self.__team_that_starts_index = random.randint(0, 1)

    @validate_arguments
    def simulate_battle(
        self,
        simulation_type: int = SimulationTypes.NORMAL
    ) -> dict:
        current_entity1_index = 0
        current_entity2_index = 0

        start_team_index = self.__team_that_starts_index
        other_team_index = (start_team_index + 1) % 2

        current_entity1 = self.__teams[start_team_index][current_entity1_index]
        current_entity2 = self.__teams[other_team_index][current_entity2_index]

        shifts = []

        if simulation_type == SimulationTypes.NORMAL:
            while True:
                while current_entity1.is_alive:
                    entity1_selected_attack = select_best_attack(
                        current_entity1.attacks,
                        current_entity2.weaknesses,
                        current_entity2.main_element
                    )

                    current_entity1_attack_data = current_entity1.attack(current_entity2, entity1_selected_attack)

                    shifts.append({
                        "team_index": start_team_index,
                        "entity_index": current_entity1_index,
                        "selected_attack": entity1_selected_attack,
                        "damage": current_entity1_attack_data["damage"],
                        "damage_type": current_entity1_attack_data["damage_type"]
                    })

                    if not current_entity2.is_alive:
                        current_entity2_index += 1

                        if current_entity2_index >= len(self.__teams[other_team_index]):
                            return dict(
                                start_team_index = start_team_index,
                                winner_index = start_team_index,
                                shifts = shifts,
                                living_dragons = [
                                    self.__teams[start_team_index].index(entity)
                                    for entity in self.__teams[start_team_index][:current_entity1_index] 
                                ]
                            )

                        current_entity2 = self.__teams[other_team_index][current_entity2_index]
                        
                    entity2_selected_attack = select_best_attack(
                        current_entity2.attacks,
                        current_entity1.weaknesses,
                        current_entity1.main_element
                    )

                    current_entity2_attack_data = current_entity2.attack(current_entity1, entity2_selected_attack)

                    shifts.append({
                        "team_index": other_team_index,
                        "entity_index": current_entity2_index,
                        "selected_attack": entity2_selected_attack,
                        "damage": current_entity2_attack_data["damage"],
                        "damage_type": current_entity2_attack_data["damage_type"]
                    })

                else:
                    current_entity1_index += 1

                    if current_entity1_index >= len(self.__teams[start_team_index]):
                        return dict(
                            start_team_index = start_team_index,
                            winner_index = other_team_index,
                            shifts = shifts,
                            living_dragons =  [
                                self.__teams[other_team_index].index(entity)
                                for entity in self.__teams[other_team_index][:current_entity2_index] 
                            ]
                        )

                    current_entity1 = self.__teams[start_team_index][current_entity1_index]
