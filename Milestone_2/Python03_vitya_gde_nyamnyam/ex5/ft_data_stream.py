import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = [
        "alice",
        "bob",
        "charlie",
        "dylan"
    ]

    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "swim",
        "climb",
        "use",
        "release"
    ]

    while True:
        yield (
            random.choice(players),
            random.choice(actions)
        )


def consume_event(events) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    generator = gen_event()

    for i in range(1000):
        event = next(generator)
        print(
            f"Event {i}: Player {event[0]} did action {event[1]}"
        )

    event_list = []

    for i in range(10):
        event_list.append(next(generator))

    print("Built list of 10 events:", event_list)

    for event in consume_event(event_list):
        print("Got event from list:", event)
        print("Remains in list:", event_list)


if __name__ == "__main__":
    main()
