"""Potions: brewed by summoning elements from near and distant modules."""
from elements import create_fire, create_water
from .elements import create_air, create_earth


def healing_potion() -> str:
    """Brew a healing potion from the earth and air elements."""
    return (
        f"Healing potion brewed with '{create_earth()}' "
        f"and '{create_air()}'"
    )


def strength_potion() -> str:
    """Brew a strength potion from the fire and water elements."""
    return (
        f"Strength potion brewed with '{create_fire()}' "
        f"and '{create_water()}'"
    )
