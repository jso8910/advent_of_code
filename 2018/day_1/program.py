def get_input():
    with open("day_1/input.txt") as f:
        return list(map(int, f.read().splitlines()))


def part_one(freq_changes):
    return sum(freq_changes)


def part_two(freq_changes):
    freq = 0
    pointer = 0
    visited = set()
    while True:
        freq += freq_changes[pointer]
        if freq in visited:
            return freq
        visited.add(freq)
        pointer += 1
        pointer %= len(freq_changes)


print(part_one(get_input()))
print(part_two(get_input()))
