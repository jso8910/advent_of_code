from datetime import datetime, timedelta
from collections import defaultdict


def get_input():
    with open("day_4/input.txt", "r") as f:
        file = f.read().splitlines()

    events = []
    for line in file:
        time = datetime.fromisoformat(line.replace("]", "[").split("[")[1])
        match line.replace("#", "").split("] ")[1].split(" "):
            case ["Guard", n, "begins", "shift"]:
                events.append((time, ("shift", int(n))))
            case ["wakes", "up"]:
                events.append((time, "wake"))
            case ["falls", "asleep"]:
                events.append((time, "asleep"))

    return events


def part_one(events):
    events = sorted(events, key=lambda x: x[0])
    guards = defaultdict(lambda: defaultdict(int))

    current_guard = None
    guard_asleep_time: datetime = None
    for event in events:
        match event[1]:
            case ("shift", n):
                current_guard = n
            case "asleep":
                guard_asleep_time = event[0]
            case "wake":
                delta = timedelta(minutes=1)
                while guard_asleep_time < event[0]:
                    guards[current_guard][guard_asleep_time.minute] += 1
                    guard_asleep_time += delta

    max_guard_asleep_time = 0
    max_guard = None
    for guard, guard_times in guards.items():
        guard_asleep_time = sum(guard_times.values())
        if guard_asleep_time > max_guard_asleep_time:
            max_guard_asleep_time = guard_asleep_time
            max_guard = guard

    max_minute_asleep_times = 0
    max_minute = None
    for minute, num_times in guards[max_guard].items():
        if num_times > max_minute_asleep_times:
            max_minute_asleep_times = num_times
            max_minute = minute

    return max_minute * max_guard


def part_two(events):
    events = sorted(events, key=lambda x: x[0])
    guards = defaultdict(lambda: defaultdict(int))

    current_guard = None
    guard_asleep_time: datetime = None
    for event in events:
        match event[1]:
            case ("shift", n):
                current_guard = n
            case "asleep":
                guard_asleep_time = event[0]
            case "wake":
                delta = timedelta(minutes=1)
                while guard_asleep_time < event[0]:
                    guards[current_guard][guard_asleep_time.minute] += 1
                    guard_asleep_time += delta

    max_minute_asleep_times = 0
    max_guard = None
    max_minute = None
    for guard in guards:
        for minute, num_times in guards[guard].items():
            if num_times > max_minute_asleep_times:
                max_minute_asleep_times = num_times
                max_guard = guard
                max_minute = minute

    return max_minute * max_guard


print(part_one(get_input()))
print(part_two(get_input()))
