"""Light validator: checks ingredients against the light spellbook."""
from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Return the ingredients followed by VALID or INVALID."""
    allowed = light_spell_allowed_ingredients()
    lowered = ingredients.lower()
    if any(ingredient in lowered for ingredient in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
