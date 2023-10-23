from pydantic import validate_call

from .config import ELEMENTS_CONFIG

@validate_call
def calculate_strongs(elements: list[str]) -> list[str]:
    strongs = []

    for element in elements:
        preview_strongs = ELEMENTS_CONFIG[element]["strongs"]

        for element in preview_strongs:
            if not element in strongs:
                strongs.append(element)

    return strongs

@validate_call
def calculate_weaknesses(first_element: str) -> list[str]:
    weaknesses = []

    for element in ELEMENTS_CONFIG.keys():
        element_strongs = ELEMENTS_CONFIG[element]["strongs"]

        if first_element in element_strongs:
            weaknesses.append(element)

    return weaknesses

__all__ = [
    "calculate_strongs",
    "calculate_weaknesses"
]