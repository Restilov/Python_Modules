from ex0 import Creature, CreatureFactory
from ex1 import (
    HealCapability,
    HealingCreatureFactory,
    TransformCapability,
    TransformCreatureFactory,
)


def test_healer(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, HealCapability):
        print(creature.heal())


def test_shifter(creature: Creature) -> None:
    print(creature.describe())
    print(creature.attack())
    if isinstance(creature, TransformCapability):
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


def test_family(factory: CreatureFactory, capability: str) -> None:
    print(f"Testing Creature with {capability} capability")
    test = test_healer if capability == "healing" else test_shifter
    print(" base:")
    test(factory.create_base())
    print(" evolved:")
    test(factory.create_evolved())


def main() -> None:
    test_family(HealingCreatureFactory(), "healing")
    print()
    test_family(TransformCreatureFactory(), "transform")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
