from day7.step import Step


def read_input():
    return tuple(
        get_intruction_steps(l)
        for l in open('input.txt').readlines()
    )


def get_intruction_steps(l):
    x = l.strip().split(' ')
    return x[1], x[7]


def initialise_steps(instructions):
    letters = {
        step
        for instruction in instructions
        for step in instruction
    }
    steps = {
        letter: Step(letter)
        for letter in letters
    }
    for p, n in instructions:
        prev_step = steps[p]
        next_step = steps[n]
        prev_step.next_steps.append(next_step)
        next_step.prev_steps.append(prev_step)
    return steps


def get_next_step(steps):
    return min((
        step
        for step in steps
        if not step.prev_steps
    ), key=lambda s: s.letter)


def complete_step(step, steps):
    for next_step in step.next_steps:
        next_step.prev_steps.remove(step)
    steps.pop(step.letter)
    return steps


def part_1(instructions):
    steps = initialise_steps(instructions)

    order = ""
    while steps:
        next_step = get_next_step(steps.values())
        order += next_step.letter
        steps = complete_step(next_step, steps)
    return order


def get_next_steps(steps, worker_count):
    doing_steps = [
        step
        for step in steps
        if step.doing
    ]
    new_step_count = worker_count - len(doing_steps)
    new_steps = sorted([
        step
        for step in steps
        if not step.doing and not step.prev_steps
    ], key=lambda s: s.letter)[:new_step_count]

    return sorted(doing_steps + new_steps, key=lambda s: s.remaining_time)


def part_2(instructions, worker_count):
    steps = initialise_steps(instructions)

    total_duration = 0
    while steps:
        doing_steps = get_next_steps(steps.values(), worker_count)
        ending_step = doing_steps[0]
        duration = ending_step.remaining_time
        total_duration += duration
        for doing_step in doing_steps[1:]:
            doing_step.doing = True
            doing_step.remaining_time -= duration
        steps = complete_step(ending_step, steps)

    return total_duration


if __name__ == '__main__':
    day7_input = read_input()

    print(f"Part 1: {part_1(day7_input)}")
    print(f"Part 2: {part_2(day7_input, worker_count=5)}")
