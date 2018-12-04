import re
from collections import defaultdict
from datetime import datetime

from day4.guard import Guard


event_regex = re.compile("\\[(.*)\\] (.*)$")
shift_regex = re.compile("Guard #(\\d+) begins shift")


def read_input():
    return sorted(tuple(
        parse_event(l.strip())
        for l in open('input.txt')
    ))


def parse_event(event):
    match = event_regex.match(event)
    dt, message = match.groups()
    return datetime.strptime(dt, "%Y-%m-%d %H:%M"), message


def parse_shift_message(shift_message):
    match = shift_regex.match(shift_message)
    if match:
        return int(match.group(1))
    return None


def execute_events(events):
    guards = defaultdict(Guard)
    current_guard = Guard()  # Create dummy guard

    for dt, message in events:
        guard_id = parse_shift_message(message)
        if guard_id:
            current_guard = guards[guard_id]
            current_guard.begin(dt)
        elif message == "falls asleep":
            current_guard.sleep(dt)
        elif message == "wakes up":
            current_guard.wake_up(dt)
        else:
            raise ValueError(message)

    return guards


def part_1(events):
    guards = execute_events(events)

    total_slept_times = (
        (guard_id, guard, sum(guard.time_slept.values()))
        for guard_id, guard in guards.items()
    )
    max_guard_id, max_guard = max(total_slept_times, key=lambda x: x[2])[:2]
    max_minute = max(max_guard.time_slept.items(), key=lambda x: x[1])[0]

    return max_guard_id * max_minute


def part_2(events):
    guards = execute_events(events)

    max_guard_id, max_minute = max((
        (guard_id, minute, slept_time)
        for guard_id, guard in guards.items()
        for minute, slept_time in guard.time_slept.items()
    ), key=lambda x: x[2])[:2]

    return max_guard_id * max_minute


if __name__ == '__main__':
    day4_input = read_input()

    print(f"Part 1: {part_1(day4_input)}")
    print(f"Part 2: {part_2(day4_input)}")
