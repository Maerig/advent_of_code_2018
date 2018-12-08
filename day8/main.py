from day8.node import Node


def read_input():
    return tuple(
        n
        for n in open('input.txt').read().split()
    )


def parse_next_node(it):
    child_count = int(next(it))
    metadata_count = int(next(it))

    children = tuple(
        parse_next_node(it)
        for _ in range(child_count)
    )
    metadata = tuple(
        int(next(it))
        for _ in range(metadata_count)
    )

    return Node(children, metadata)


def parse_tree(raw_input):
    return parse_next_node(iter(raw_input))


def part_1(tree):
    return tree.metadata_sum()


def part_2(tree):
    return tree.value()


if __name__ == '__main__':
    day8_input = read_input()
    day8_tree = parse_tree(day8_input)

    print(f"Part 1: {part_1(day8_tree)}")
    print(f"Part 2: {part_2(day8_tree)}")
