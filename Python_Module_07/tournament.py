from typing import List, Tuple

from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)

Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    fighters = [
        (factory.create_base(), strategy) for factory, strategy in opponents
    ]
    for index, (creature, strategy) in enumerate(fighters):
        for other, other_strategy in fighters[index + 1:]:
            print()
            print("* Battle *")
            print(creature.describe())
            print(" vs.")
            print(other.describe())
            print(" now fight!")
            try:
                for action in strategy.act(creature):
                    print(action)
                for action in other_strategy.act(other):
                    print(action)
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (healing, defensive)])

    print()
    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (healing, defensive)])

    print()
    print("Tournament 2 (multiple)")
    print(
        " [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]"
    )
    battle([(aqua, normal), (healing, defensive), (transform, aggressive)])


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
