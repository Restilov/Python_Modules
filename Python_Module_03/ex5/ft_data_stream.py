import random
from typing import Generator


PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "move", "grab", "use", "climb", "swim", "sleep",
           "eat", "release", "attack"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        idx = random.randint(0, len(events) - 1)
        event = events[idx]
        events.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_gen = gen_event()
    for i in range(1000):
        name, action = next(event_gen)
        print(f"Event {i}: Player {name} did action {action}")

    event_list: list[tuple[str, str]] = []
    event_gen2 = gen_event()
    for _ in range(10):
        event_list.append(next(event_gen2))
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


main()
