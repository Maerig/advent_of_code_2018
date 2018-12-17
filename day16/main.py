import re

from day16.processor import Processor


state_regex = re.compile("(?:Before|After):\\s+\\[(.+)\\]")


def read_input():
    def parse_state(state):
        match = state_regex.match(state)
        return [
            int(n)
            for n in match.group(1).split(',')
        ]

    def parse_command(command):
        return [
            int(n)
            for n in command.split(' ')
        ]

    lines = (
        l.strip()
        for l in open('samples.txt').readlines()
    )

    samples = []
    while True:
        try:
            before = parse_state(next(lines))
            command = parse_command(next(lines))
            after = parse_state(next(lines))
            samples.append((command, before, after))
            next(lines)
        except StopIteration:
            break

    commands = [
        parse_command(command)
        for command in open('commands.txt').readlines()
    ]

    return samples, commands


def get_compatible_commands(command, before, after):
    compatibles = set()
    processor = Processor()
    _, a, b, c = command
    for commands_name, command_exec in processor.commands_by_name.items():
        processor.registers = before.copy()
        command_exec(a, b, c)
        if processor.registers == after:
            compatibles.add(commands_name)
    return compatibles


def get_compatibilities(samples):
    return tuple(
        (sample, get_compatible_commands(*sample))
        for sample in samples
    )


def part_1(samples):
    compatibilities = get_compatibilities(samples)
    return sum(
        len(sample_compatibilites) >= 3
        for _, sample_compatibilites in compatibilities
    )


def remove_opcode_command_pair(opcode, command, opcode_compatibilities, command_compatibilities):
    for opcode in opcode_compatibilities:
        opcode_compatibilities[opcode].discard(command)
    for command in command_compatibilities:
        command_compatibilities[command].discard(opcode)


def infer_configuration(samples):
    all_command_names = set(Processor().commands_by_name.keys())
    command_count = len(all_command_names)

    opcode_compatibilities = {
        i: all_command_names.copy()
        for i in range(command_count)
    }
    command_compatibilities = {
        command_name: set(range(command_count))
        for command_name in all_command_names
    }

    sample_compatibilities = get_compatibilities(samples)
    for sample, compatible_command_names in sample_compatibilities:
        sample_command = sample[0]
        opcode = sample_command[0]
        incompatible_command_names = all_command_names - compatible_command_names
        opcode_compatibilities[opcode] = opcode_compatibilities[opcode] - incompatible_command_names

    command_by_opcode = {}
    while len(command_by_opcode) < command_count:
        for opcode, compatible_commands in opcode_compatibilities.items():
            if len(compatible_commands) == 1:
                command = compatible_commands.pop()
                command_by_opcode[opcode] = command
                remove_opcode_command_pair(
                    opcode,
                    command,
                    opcode_compatibilities,
                    command_compatibilities
                )

        for command, compatible_opcodes in command_compatibilities.items():
            if len(compatible_opcodes) == 1:
                opcode = compatible_opcodes[0]
                command_by_opcode[opcode] = command
                remove_opcode_command_pair(
                    opcode,
                    command,
                    opcode_compatibilities,
                    command_compatibilities
                )

    return command_by_opcode


def save_configuration(configuration, path="config.txt"):
    with open(path, "w") as config_file:
        for opcode in sorted(configuration.keys()):
            config_file.write(
                f"{opcode}={configuration[opcode]}\n"
            )
    return path


def part_2(samples, commands):
    configuration = infer_configuration(samples)
    path = save_configuration(configuration)

    processor = Processor()
    processor.load_configuration(path)
    for command in commands:
        processor.run_command(*command)
    return processor.registers[0]


if __name__ == '__main__':
    samples, commands = read_input()

    print(f"Part 1: {part_1(samples)}")
    print(f"Part 2: {part_2(samples, commands)}")
