from collections import Counter
from utils.vector import Vector


SIZE = 50


def read_input():
    acres = {}
    for j, l in enumerate(open('input.txt').readlines()):
        for i, c in enumerate(l.strip()):
            acres[Vector(j, i)] = c
    return acres


def get_adjacent_acres(pos, acres):
    for j in range(-1, 2):
        for i in range(-1, 2):
            if (j, i) == (0, 0):
                continue
            adj_pos = pos + Vector(j, i)
            if 0 <= adj_pos[0] < SIZE and 0 <= adj_pos[1] < SIZE:
                yield acres[adj_pos]


def transform(current_acre, adjacent_acres):
    counts = Counter(adjacent_acres)
    if current_acre == ".":
        return "|" if counts["|"] >= 3 else "."
    if current_acre == "|":
        return "#" if counts["#"] >= 3 else "|"
    if current_acre == "#":
        return "#" if counts["|"] >= 1 and counts["#"] >= 1 else "."


def run(initial_acres, goal):
    acres = initial_acres.copy()
    state_history = [acres.copy()]
    t = 0
    while t < goal:
        t += 1
        new_acres = {}
        for y in range(SIZE):
            for x in range(SIZE):
                pos = Vector(y, x)
                adjacent_acres = get_adjacent_acres(pos, acres)
                new_acres[pos] = transform(acres[pos], adjacent_acres)
        if new_acres in state_history:
            cycle_duration = t - state_history.index(new_acres)
            remaining = goal - t
            t += (remaining // cycle_duration) * cycle_duration
        else:
            state_history.append(new_acres)
        acres = new_acres
    counts = Counter(acres.values())
    return counts["|"] * counts["#"]


def part_1(acres):
    return run(acres, 10)


def part_2(acres):
    return run(acres, 1000000000)


if __name__ == '__main__':
    day18_input = read_input()

    print(f"Part 1: {part_1(day18_input)}")
    print(f"Part 2: {part_2(day18_input)}")
