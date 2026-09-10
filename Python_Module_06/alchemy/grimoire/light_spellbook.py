"""Light spellbook: records spells, safely validated (no circular import)."""


def light_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed by light magic."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a light spell if its ingredients are validated."""
    # Deferred (local) import: the cycle is broken because
    # light_validator is only loaded when the function is called,
    # not while this module is being initialized.
    from .light_validator import validate_ingredients

    report = validate_ingredients(ingredients)
    if report.endswith("- VALID"):
        return f"Spell recorded: {spell_name} ({report})"
    return f"Spell rejected: {spell_name} ({report})"
