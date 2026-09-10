"""Public interface of the alchemy package.

Only a part of the package is exposed on purpose: create_earth stays
hidden behind the module interface (see ft_alembic_4.py).
"""
from .elements import create_air
from .potions import healing_potion, strength_potion
from .potions import healing_potion as heal
from .transmutation import lead_to_gold

__all__ = [
    "create_air",
    "healing_potion",
    "strength_potion",
    "heal",
    "lead_to_gold",
]
