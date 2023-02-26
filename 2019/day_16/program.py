from itertools import cycle


def get_input():
    with open("day_16/input.txt", "r") as f:
        return list(map(int, f.read()))


def part_one(signal):
    pattern = [0, 1, 0, -1]
    for i in range(100):
        new_signal = []
        for idx, digit in enumerate(signal):
            pattern_for_dig = [n for n in pattern for _ in range(idx + 1)]
            pattern_cycle = cycle(pattern_for_dig)
            next(pattern_cycle)
            new_signal.append(0)
            for mul, dig in zip(pattern_cycle, signal):
                new_signal[-1] += dig * mul
            new_signal[-1] = abs(new_signal[-1]) % 10
        signal = new_signal

    return "".join(map(str, signal[:8]))


def part_two(signal):
    signal *= 10_000
    offset = int("".join(map(str, signal[:7])))
    signal = signal[offset:]
    pattern = [0, 1, 0, -1]
    for i in range(100):
        for idx, digit in reversed(list(enumerate(signal))):
            if idx == 0:
                continue
            signal[idx - 1] = signal[idx] + signal[idx - 1]
            signal[idx - 1] %= 10

    return "".join(map(str, signal[:8]))


print(part_one(get_input()))
print(part_two(get_input()))
