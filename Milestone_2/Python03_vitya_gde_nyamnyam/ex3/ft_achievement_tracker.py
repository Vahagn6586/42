import random

ACHIEVEMENTS = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "Hidden Path Finder",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer"
]


def gen_player_achievements() -> set[str]:
    number = random.randint(3, 9)
    return set(random.sample(ACHIEVEMENTS, number))


def main() -> None:
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()

    distinct_achievements = (
        alice
        | bob
        | charlie
        | dylan
    )

    print("All distinct achievements:", distinct_achievements)
    print()

    common_achievements = (
        alice
        & bob
        & charlie
        & dylan
    )

    print("Common achievements:", common_achievements)
    print()

    only_alice = alice - bob - charlie - dylan
    only_bob = bob - alice - charlie - dylan
    only_charlie = charlie - alice - bob - dylan
    only_dylan = dylan - alice - bob - charlie

    print("Only Alice has:", only_alice)
    print("Only Bob has:", only_bob)
    print("Only Charlie has:", only_charlie)
    print("Only Dylan has:", only_dylan)
    print()

    print("Alice is missing:", distinct_achievements - alice)
    print("Bob is missing:", distinct_achievements - bob)
    print("Charlie is missing:", distinct_achievements - charlie)
    print("Dylan is missing:", distinct_achievements - dylan)


if __name__ == "__main__":
    main()
