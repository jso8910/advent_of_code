def get_input():
    with open("day_6/input.txt", "r") as f:
        return list(map(int, f.read().split()))


def part_one(banks):
    redistributions = 0
    seen = set()
    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        redistributions += 1
        max_blocks = max(banks)
        max_index = banks.index(max_blocks)
        banks[max_index] = 0
        for i in range(max_blocks):
            banks[(max_index + i + 1) % len(banks)] += 1
    return redistributions


def part_two(banks):
    redistributions = 0
    seen = set()
    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        redistributions += 1
        max_blocks = max(banks)
        max_index = banks.index(max_blocks)
        banks[max_index] = 0
        for i in range(max_blocks):
            banks[(max_index + i + 1) % len(banks)] += 1

    redistributions = 0
    seen = set()
    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        redistributions += 1
        max_blocks = max(banks)
        max_index = banks.index(max_blocks)
        banks[max_index] = 0
        for i in range(max_blocks):
            banks[(max_index + i + 1) % len(banks)] += 1
    return redistributions


print(part_one(get_input()))
print(part_two(get_input()))
