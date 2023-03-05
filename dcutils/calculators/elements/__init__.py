from pydantic import validate_arguments

from .config import ELEMENTS_CONFIG

@validate_arguments
def calculate_strongs(elements: list[str]) -> list[str]:
    strongs = []

    for element in elements:
        strong = ELEMENTS_CONFIG[element]["strongs"]

        for element in strong:
            if not element in strongs:
                strongs.append(element)

    return strongs

@validate_arguments
def calculate_weaknesses(first_element: str) -> list[str] | list:
    weaknesses = []

    for key in ELEMENTS_CONFIG.keys():
        if first_element in ELEMENTS_CONFIG[key]["strongs"]:
            weaknesses.append(key)

    return weaknesses

__all__ = [
    calculate_strongs,
    calculate_weaknesses
]