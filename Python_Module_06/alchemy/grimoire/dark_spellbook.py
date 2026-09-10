"""Dark spellbook: cursed twin, imports its validator at module level."""
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Return the ingredients allowed by dark magic."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Record a dark spell if its ingredients are validated."""
    report = validate_ingredients(ingredients)
    if report.endswith("- VALID"):
        return f"Spell recorded: {spell_name} ({report})"
    return f"Spell rejected: {spell_name} ({report})"
