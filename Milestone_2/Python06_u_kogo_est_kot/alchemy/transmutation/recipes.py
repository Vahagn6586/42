from alchemy import create_air
from ..potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    r = "Recipe transmuting Lead to Gold: brew"
    r += f" '{create_air()}'"
    r += " and "
    r += f"'{strength_potion()}' "
    r += "mixed with" + f" '{create_fire()}'"
    return r
