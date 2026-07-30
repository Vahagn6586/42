from elements import create_fire, create_water
from alchemy.elements import create_air, create_earth


def healing_potion() -> str:
    r = "Healing potion brewed with" + " " + f"'{create_earth()}'"
    r += " and "
    r += f"'{create_air()}'"
    return r


def strength_potion() -> str:
    r = "Strength potion brewed with" + " " + f"'{create_fire()}'"
    r += " and "
    r += f"'{create_water()}'"
    return r
