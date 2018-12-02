from collections import Counter


def read_input():
    return tuple(
        l.strip()
        for l in open('input.txt')
    )


def part_1(box_ids):
    counts = tuple(
        Counter(Counter(box_id).values())
        for box_id in box_ids
    )
    return sum(
        1 if count[2] >= 1 else 0
        for count in counts
    ) * sum(
        1 if count[3] >= 1 else 0
        for count in counts
    )


def part_2(box_ids):
    def common(s1, s2):
        return tuple(a for a, b in zip(s1, s2) if a == b)

    for i in range(0, len(box_ids)):
        box_id_1 = box_ids[i]
        target_length = len(box_id_1) - 1
        for j in range(i + 1, len(box_ids)):
            box_id_2 = box_ids[j]
            common_part = common(box_id_1, box_id_2)
            if len(common_part) == target_length:
                return ''.join(common_part)


if __name__ == '__main__':
    day2_input = read_input()

    print(f"Part 1: {part_1(day2_input)}")
    print(f"Part 2: {part_2(day2_input)}")
