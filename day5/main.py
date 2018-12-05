from functools import reduce

from utils.progress import show_progress


def read_input():
    return open('input.txt').read()


def react(current_polymer, unit):
    if not current_polymer:
        return [unit]

    tail = current_polymer[-1]
    if tail.lower() != unit.lower() or tail == unit:
        return current_polymer + [unit]
    return current_polymer[:-1]


def run_reactions(polymer):
    current_polymer = list(polymer)
    while True:
        new_polymer = reduce(react, polymer, [])
        if len(new_polymer) == len(current_polymer):
            return current_polymer
        current_polymer = new_polymer


def part_1(polymer):
    return len(run_reactions(polymer))


def part_2(polymer):
    final_polymer = run_reactions(polymer)

    unit_types = {
        unit.lower()
        for unit in final_polymer
    }

    sizes = {}
    for unit_type in unit_types:
        show_progress(len(sizes) / len(unit_types))
        shortened_polymer = list(
            unit
            for unit in final_polymer
            if unit.lower() != unit_type
        )
        polymer_size = len(run_reactions(shortened_polymer))
        sizes[unit_type] = polymer_size
    show_progress(1)

    return min(sizes.values())


if __name__ == '__main__':
    day5_input = read_input()

    print(f"Part 1: {part_1(day5_input)}")
    print(f"\nPart 2: {part_2(day5_input)}")
