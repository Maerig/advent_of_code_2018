from collections import Counter
from day3.claim import Claim


def read_input():
    return tuple(
        Claim(l)
        for l in open('input.txt')
    )


def get_used_count(claims):
    return Counter(
        square
        for claim in claims
        for square in claim.get_squares()
    )


def part_1(claims):
    used_count = get_used_count(claims)

    return sum(
        1
        for used_count in used_count.values()
        if used_count >= 2
    )


def overlaps(claim, used_count):
    squares = claim.get_squares()
    for square in squares:
        if used_count[square] > 1:
            return True
    return False


def part_2(claims):
    used_count = get_used_count(claims)
    for claim in claims:
        if not overlaps(claim, used_count):
            return claim.id


if __name__ == '__main__':
    day3_input = read_input()

    print(f"Part 1: {part_1(day3_input)}")
    print(f"Part 2: {part_2(day3_input)}")
