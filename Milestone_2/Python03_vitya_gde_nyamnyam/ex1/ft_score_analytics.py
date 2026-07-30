import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = []
    for i in sys.argv[1:]:
        try:
            scores.append(int(i))
        except ValueError:
            print(f"Invalid parameter: {i}")

    if len(scores) == 0:
        print("No scores provided.", sys.argv)
        return

    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", sum(scores)/len(scores))
    print("Highest score:", max(scores))
    print("Lowest score:", min(scores))
    print("Score range:", max(scores) - min(scores))


if __name__ == "__main__":
    main()
