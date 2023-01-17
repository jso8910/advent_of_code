from collections import deque


def get_input():
    with open("day_19/input.txt", "r") as f:
        return int(f.read())


def part_one(num_elves):
    queue = deque([elf, 1] for elf in range(1, num_elves + 1))
    while len(queue) > 1:
        queue.rotate(-1)
        popped = queue.popleft()
        queue[-1][1] += popped[1]

    return queue[0][0]


def part_two(num_elves):
    queue = deque([elf, 1] for elf in range(1, num_elves + 1))
    current_elf = 1
    elf_size = num_elves
    coff = 0
    while len(queue) > 1:
        n = (elf_size // 2) - coff
        queue.rotate(-n)
        popped = queue.popleft()

        coff = (coff + n - 1) % elf_size
        elf_size -= 1

    return queue[0][0]


print(part_one(get_input()))
print(part_two(get_input()))
