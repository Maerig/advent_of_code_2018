import re
from collections import Counter

from day9.marble import Marble
from utils.progress import show_progress


def read_input():
    raw_input = open('input.txt').read()
    match = re.match(
        "(\\d+) players; last marble is worth (\\d+) points",
        raw_input
    )
    return tuple(
        int(n)
        for n in match.groups()
    )


def play(player_count, marble_count):
    scores = Counter()
    current_marble = None
    for i in range(marble_count + 1):
        show_progress(i / marble_count)
        if not current_marble:
            current_marble = Marble(i)
            current_marble.prev_marble = current_marble.next_marble = current_marble
        elif i % 23 != 0:
            new_marble = Marble(i)
            current_marble.next_marble.add_next(new_marble)
            current_marble = new_marble
        else:
            player_id = i % player_count
            scores[player_id] += i
            removed_marble = current_marble.get_prev(7)
            current_marble = removed_marble.next_marble
            scores[player_id] += removed_marble.remove()

    return max(scores.values())


def part_1(player_count, marble_count):
    return play(player_count, marble_count)


def part_2(player_count, marble_count):
    return play(player_count, 100 * marble_count)


if __name__ == '__main__':
    day9_input = read_input()

    print(f"\nPart 1: {part_1(*day9_input)}")
    print(f"\nPart 2: {part_2(*day9_input)}")
