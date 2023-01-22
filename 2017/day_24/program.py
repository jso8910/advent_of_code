from itertools import permutations


def get_input():
    with open("day_24/input.txt", "r") as f:
        file = f.read().splitlines()

    ports = []
    for line in file:
        ports.append(tuple(map(int, line.split("/"))))

    return ports


def dfs(ports, start, paths=[], path=[], seen=set(), p2=False):
    path.append(start)
    next_ports = [port for port in ports if port not in path and (port[1], port[0]) not in path and any(
        port[i] == start[1] for i in range(2))]
    # current_strength = sum(sum(path, start=()))
    # if current_strength + sum(sum([p for p in ports if p not in path and (p[1], p[0])], start=())) <= max(paths, default=0):
    #     return
    combo = tuple(set(path))
    if combo in seen:
        return
    seen.add(combo)
    if not next_ports:
        if not p2:
            paths.append(sum(sum(path, start=())))
        else:
            paths.append((
                sum(sum(path, start=())),
                len(path)
            ))
    for port in next_ports:
        if port[0] != start[1]:
            port = (port[1], port[0])
        dfs(ports, port, paths=paths, path=path.copy(), p2=p2)


def part_one(ports):
    paths = []
    seen = set()
    starts = [port for port in ports if any(
        port[i] == 0 for i in range(2))]
    for start in starts:
        if start[0] != 0:
            start = (start[1], start[0])
        dfs(ports, start, paths=paths, path=[], seen=seen,)

    return max(paths)


def part_two(ports):
    paths = []
    seen = set()
    starts = [port for port in ports if any(
        port[i] == 0 for i in range(2))]
    for start in starts:
        if start[0] != 0:
            start = (start[1], start[0])
        dfs(ports, start, paths=paths, path=[], seen=seen, p2=True)
    max_len = max(p[1] for p in paths)
    return max(p[0] for p in paths if p[1] == max_len)


print(part_one(get_input()))
print(part_two(get_input()))
