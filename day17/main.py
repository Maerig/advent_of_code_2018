from collections import defaultdict
from utils.vector import Vector

import re


def read_input():
    regex_1 = re.compile("x=(\\d+), y=(\\d+)\\.\\.(\\d+)")
    regex_2 = re.compile("y=(\\d+), x=(\\d+)\\.\\.(\\d+)")

    ground = defaultdict(lambda: ".")
    ground[Vector(500, 0)] = "~"

    x_values = set()
    y_values = set()

    for l in open('input.txt'):
        match_1 = regex_1.match(l.strip())
        if match_1:
            x, y1, y2 = (int(n) for n in match_1.groups())
            x_values.add(x)
            for y in range(y1, y2 + 1):
                ground[Vector(x, y)] = "#"
                y_values.add(y)
        else:
            match_2 = regex_2.match(l.strip())
            y, x1, x2 = (int(n) for n in match_2.groups())
            y_values.add(y)
            for x in range(x1, x2 + 1):
                ground[Vector(x, y)] = "#"
                x_values.add(x)
    return ground, min(x_values), max(x_values), min(y_values), max(y_values)


def get_water_row(pos, ground):
    water_row = set()
    for direction in (Vector(-1, 0), Vector(1, 0)):
        current_pos = pos
        while ground[current_pos] not in (".", "#"):
            water_row.add(current_pos)
            current_pos += direction
    return water_row


def update_oveflowing_row(pos, ground):
    for water_pos in get_water_row(pos, ground):
        ground[water_pos] = "|"


def fall(pos, ground, end):
    while True:
        pos += Vector(0, 1)
        if end(pos):
            return
        if ground[pos] != ".":
            break
        ground[pos] = "|"
    if ground[pos] == "#":
        pos -= Vector(0, 1)
    ground[pos] = "~"
    is_overflowing = spread_bilateral(pos, ground, end)
    if not is_overflowing:
        rise(pos, ground, end)


def spread(pos, ground, direction, end):
    while True:
        pos += direction
        if ground[pos] == "#":
            return False
        else:
            pos_below = pos + Vector(0, 1)
            if ground[pos_below] == ".":
                ground[pos] = "|"
                fall(pos, ground, end)
                has_filled = (ground[pos_below] == "~")
                return not has_filled
            elif ground[pos_below] == "|":
                return True
            ground[pos] = "~"


def spread_bilateral(pos, ground, end):
    is_overflowing_left = spread(pos, ground, Vector(-1, 0), end)
    is_overflowing_right = spread(pos, ground, Vector(1, 0), end)
    is_overflowing = is_overflowing_left or is_overflowing_right
    if is_overflowing:
        update_oveflowing_row(pos, ground)
    return is_overflowing


def rise(pos, ground, end):
    while True:
        pos += Vector(0, -1)
        if ground[pos] in ("~", "#"):
            return
        else:
            ground[pos] = "~"
            is_overflowing = spread_bilateral(pos, ground, end)
            if is_overflowing:
                return


def print_ground(ground, min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(ground[Vector(x, y)], end="")
        print()


def flow(ground, max_y):
    def end(pos):
        x, y = pos
        return y > max_y

    water_pos = Vector(500, 0)
    fall(water_pos, ground, end)
    return ground


def part_1(ground):
    return sum(
        1
        for k, v in ground.items()
        if v in ("~", "|") and min_y <= k[1] <= max_y
    )


def part_2(ground):
    return sum(
        1
        for k, v in ground.items()
        if v == "~" and min_y <= k[1] <= max_y
    )


if __name__ == '__main__':
    ground, min_x, max_x, min_y, max_y = read_input()
    ground = flow(ground, max_y)
    #print_ground(ground, min_x, max_x, min_y, max_y)

    print(f"Part 1: {part_1(ground)}")
    print(f"Part 2: {part_2(ground)}")
