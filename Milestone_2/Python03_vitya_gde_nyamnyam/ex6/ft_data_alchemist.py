import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]

    print("Initial list of players:", players)

    capitalized_players = [
        name.capitalize()
        for name in players
    ]

    print(
        "New list with all names capitalized:",
        capitalized_players
    )

    only_capitalized = [
        name
        for name in players
        if name[0].isupper()
    ]

    print(
        "New list of capitalized names only:",
        only_capitalized
    )

    scores = {
        name: random.randint(1, 1000)
        for name in capitalized_players
    }

    print("Score dict:", scores)

    average = sum(scores.values()) / len(scores)

    print(
        f"Score average is {round(average, 2)}"
    )

    high_scores = {
        name: score
        for name, score in scores.items()
        if score > average
    }

    print("High scores:", high_scores)


if __name__ == "__main__":
    main()
