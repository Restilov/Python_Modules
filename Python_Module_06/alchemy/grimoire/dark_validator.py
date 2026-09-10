"""Dark validator: imports the dark spellbook at module level. Kaboom!"""
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Return the ingredients followed by VALID or INVALID."""
    allowed = dark_spell_allowed_ingredients()
    lowered = ingredients.lower()
    if any(ingredient in lowered for ingredient in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
