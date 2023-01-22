from collections import deque


def get_input():
    with open("day_14/input.txt", "r") as f:
        return f.read()


def part_one(key):
    set_bits = 0
    for i in range(128):
        lengths = list(map(ord, (str(key) + "-" + str(i)).replace(
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
        set_bits += sum([bin(block)[2:].count("1") for block in block_results])
        # return "".join([str(hex(block))[2:].zfill(2) for block in block_results])
    return set_bits


def part_two(key):
    grid = {}
    for row in range(128):
        lengths = list(map(ord, (str(key) + "-" + str(row)).replace(
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
        for idx, char in enumerate(("".join([bin(block)[2:].zfill(8) for block in block_results]))):
            grid[(row, idx)] = char == "1"

    groups = 0
    while any(grid.values()):
        groups += 1
        start = list(grid.keys())[list(grid.values()).index(True)]
        grid[start] = False
        queue = [start]
        while queue:
            x, y = queue.pop()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (x + dx, y + dy) in grid and grid[(x + dx, y + dy)]:
                    grid[(x + dx, y + dy)] = False
                    queue.append((x + dx, y + dy))
    return groups


print(part_one(get_input()))
print(part_two(get_input()))
