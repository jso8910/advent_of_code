from collections import deque


def get_input():
    with open("day_10/input.txt", "r") as f:
        return list(map(int, f.read().split(",")))


def part_one(lengths):
    rope = deque(range(256))
    # rope = list(range(255))
    skip_size = 0
    current_pos_offset = 0
    for length in lengths:
        rope = deque(list(reversed(list(rope)[:length])) + list(rope)[length:])
        rope.rotate(-(length + skip_size))
        current_pos_offset += length + skip_size
        current_pos_offset %= len(rope)
        skip_size += 1

    rope.rotate(current_pos_offset)
    return rope[0] * rope[1]


def part_two(lengths):
    lengths = list(map(ord, str(lengths)[1:-1].replace(
        " ", ""))) + [17, 31, 73, 47, 23]
    rope = deque(range(256))
    skip_size = 0
    current_pos_offset = 0
    for i in range(64):
        for length in lengths:
            rope = deque(
                list(reversed(list(rope)[:length])) + list(rope)[length:])
            rope.rotate(-(length + skip_size))
            current_pos_offset += length + skip_size
            current_pos_offset %= len(rope)
            skip_size += 1

    rope.rotate(current_pos_offset)

    block_results = []
    result = 0
    for idx, char in enumerate(rope):
        result ^= char
        if idx % 16 == 15:
            block_results.append(result)
            result = 0
    return "".join([str(hex(block))[2:].zfill(2) for block in block_results])


print(part_one(get_input()))
print(part_two(get_input()))
