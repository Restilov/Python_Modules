from abc import ABC, abstractmethod
from typing import List

from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    ...


class BattleStrategy(ABC):
    label = "abstract"

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> List[str]:
        ...

    def _reject(self, creature: Creature) -> InvalidStrategyError:
        return InvalidStrategyError(
            f"Invalid Creature '{creature.name}' "
            f"for this {self.label} strategy"
        )


class NormalStrategy(BattleStrategy):
    label = "normal"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> List[str]:
        if not self.is_valid(creature):
            raise self._reject(creature)
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    label = "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> List[str]:
        if not isinstance(creature, TransformCapability):
            raise self._reject(creature)
        return [creature.transform(), creature.attack(), creature.revert()]


class DefensiveStrategy(BattleStrategy):
    label = "defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> List[str]:
        if not isinstance(creature, HealCapability):
            raise self._reject(creature)
        return [creature.attack(), creature.heal()]
