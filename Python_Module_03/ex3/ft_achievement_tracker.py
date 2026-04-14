import random


ALL_ACHIEVEMENTS = [
    "First Steps", "Boss Slayer", "Speed Runner", "Collector Supreme",
    "Master Explorer", "Untouchable", "World Savior", "Crafting Genius",
    "Strategist", "Survivor", "Treasure Hunter", "Unstoppable",
    "Sharp Mind", "Hidden Path Finder", "Dragon Tamer", "Pacifist",
    "Night Owl", "Speedster", "Legend", "Completionist"
]


def gen_player_achievements() -> set[str]:
    count = random.randint(4, 12)
    return set(random.sample(ALL_ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_achievements: set[str] = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    print(f"All distinct achievements: {all_achievements}")

    common: set[str] = set(ALL_ACHIEVEMENTS)
    for achievements in players.values():
        common = common.intersection(achievements)
    print(f"Common achievements: {common}")

    for name, achievements in players.items():
        others: set[str] = set()
        for other_name, other_ach in players.items():
            if other_name != name:
                others = others.union(other_ach)
        unique = achievements.difference(others)
        print(f"Only {name} has: {unique}")

    for name, achievements in players.items():
        missing = all_achievements.difference(achievements)
        print(f"{name} is missing: {missing}")


main()
