"""Public interface of the grimoire: only light magic is safe to expose."""
from .light_spellbook import (
    light_spell_allowed_ingredients,
    light_spell_record,
)

__all__ = ["light_spell_allowed_ingredients", "light_spell_record"]
