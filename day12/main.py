def read_input():
    text = tuple(
        l.strip()
        for l in open('input.txt').readlines()
    )

    initial_state = list(
        x == "#"
        for x in text[0].split(' ')[2]
    )
    rules = {
        tuple(
            y == "#"
            for y in x.split(' ')[0]
        ): x.split(' ')[2] == "#"
        for x in text[2:]
    }

    return initial_state, rules


def trim_pots(pots, zero):
    new_zero = zero

    removed_indices = set()
    i = 0
    while not pots[i]:
        removed_indices.add(i)
        new_zero -= 1
        i += 1

    i = len(pots) - 1
    while not pots[i]:
        removed_indices.add(i)
        i -= 1

    new_pots = [
        pot
        for (i, pot) in enumerate(pots)
        if i not in removed_indices
    ]

    return new_pots, new_zero


def run(initial_state, rules, iterations):
    state = initial_state
    zero = 0
    state_history = []
    zero_history = []
    step = 0
    while step < iterations:
        state = [False, False, False, False] + state + [False, False, False, False]
        new_state = []
        l = len(state)
        for i in range(2, l - 2):
            batch = tuple(
                state[j]
                for j in range(i - 2, i + 3)
            )
            new_state.append(rules.get(batch, False))
        zero += 2
        state, zero = trim_pots(new_state, zero)
        if state not in state_history:
            state_history.append(state)
            zero_history.append(zero)
        else:
            # Skip
            prev_state_index = state_history.index(state)
            cycle_iterations = step - prev_state_index
            remaining = iterations - step - 1
            step_skipped = (remaining - (remaining % cycle_iterations))
            step += step_skipped
            cycle_count = remaining // cycle_iterations
            zero += cycle_count * (zero - zero_history[prev_state_index])
        step += 1

    return sum(i - zero for i, x in enumerate(state) if x)


def part_1(initial_state, rules):
    return run(initial_state, rules, iterations=20)


def part_2(initial_state, rules):
    return run(initial_state, rules, iterations=50000000000)


if __name__ == '__main__':
    initial_state, rules = read_input()

    print(f"Part 1: {part_1(initial_state, rules)}")
    print(f"Part 2: {part_2(initial_state, rules)}")
