from hashlib import md5
from collections import deque


def get_input():
    with open("day_17/input.txt", "r") as f:
        return f.read()


def gen_hash(path, passcode):
    return md5((passcode + "".join(path)).encode('utf-8')).hexdigest()


def part_one(passcode):
    queue = deque([(0 + 0j, "")])
    visited = set()
    while queue:
        node = queue.popleft()
        if node[0] == 3 + 3j:
            return node[1]

        hash = gen_hash(node[1], passcode)
        for dir in "UDLR":
            match dir:
                case "U":
                    new_node = node[0] - 1j
                case "D":
                    new_node = node[0] + 1j
                case "L":
                    new_node = node[0] - 1
                case "R":
                    new_node = node[0] + 1

            if new_node.real < 0 or new_node.real > 3 or new_node.imag < 0 or new_node.imag > 3:
                continue
            if hash["UDLR".index(dir)] in "bcdef" and new_node not in visited:
                queue.append((new_node, node[1] + dir))
                visited.add((new_node, node[1] + dir))


def part_two(passcode):
    queue = deque([(0 + 0j, "")])
    visited = set()
    longest_path = 0
    while queue:
        node = queue.popleft()
        if node[0] == 3 + 3j:
            longest_path = max(longest_path, len(node[1]))
            continue

        hash = gen_hash(node[1], passcode)
        for dir in "UDLR":
            match dir:
                case "U":
                    new_node = node[0] - 1j
                case "D":
                    new_node = node[0] + 1j
                case "L":
                    new_node = node[0] - 1
                case "R":
                    new_node = node[0] + 1

            if new_node.real < 0 or new_node.real > 3 or new_node.imag < 0 or new_node.imag > 3:
                continue
            if hash["UDLR".index(dir)] in "bcdef" and new_node not in visited:
                queue.append((new_node, node[1] + dir))
                visited.add((new_node, node[1] + dir))

    return longest_path


print(part_one(get_input()))
print(part_two(get_input()))
