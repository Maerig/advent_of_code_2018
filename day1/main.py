def read_input():
    return tuple(
        int(l)
        for l in open('input.txt')
    )


def part_1(deltas):
    return sum(deltas)


def part_2(deltas):
    frequency = 0
    frequencies = set()

    while True:
        for delta in deltas:
            frequencies.add(frequency)
            frequency += delta
            if frequency in frequencies:
                return frequency


if __name__ == '__main__':
    day1_input = read_input()

    print(f"Part 1: {part_1(day1_input)}")
    print(f"Part 2: {part_2(day1_input)}")
