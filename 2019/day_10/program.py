from sympy import pi, tan, atan2
from fractions import Fraction
from collections import defaultdict
ARBITRARY_CONSTANT_FOR_INFINITY = 10_000_000


def get_input():
    with open("day_10/input.txt", "r") as f:
        file = f.read().splitlines()

    grid = defaultdict(bool)
    for idx, line in enumerate(file):
        for cidx, char in enumerate(line):
            if char == "#":
                grid[(cidx, idx)] = True

    return grid


def asteroid_is_visible(grid, start, end):
    # Div by zero error otherwise
    if start[0] == end[0]:
        dy = 1 if end[1] > start[1] else -1
        dx = 0
    else:
        dy, dx = Fraction((end[1] - start[1]),
                          (end[0] - start[0])).as_integer_ratio()

        # Python fractions always make the denominator positive
        if end[0] < start[0]:
            dy, dx = -dy, -dx
    point = end
    while point != start:
        point = (point[0] - dx, point[1] - dy)
        if point in grid and grid[point] and point != end and point != start:
            return False
    return True


def part_one(grid):
    max_seen = -1
    asteroids = [p for p in grid if grid[p]]
    for start_asteroid in asteroids:
        seen = 0
        for asteroid in asteroids:
            if asteroid == start_asteroid:
                continue
            if asteroid_is_visible(grid, start_asteroid, asteroid):
                seen += 1
        max_seen = max(seen, max_seen)

    return max_seen


def calc_slope(start, end, positive=True):
    if start[0] == end[0]:
        return ARBITRARY_CONSTANT_FOR_INFINITY*(1 if positive else -1)
    else:
        return (start[1] - end[1])/(start[0] - end[0])


def part_two(grid):
    max_seen = -1
    max_seen_point = None
    asteroids = [p for p in grid if grid[p]]
    for start_asteroid in asteroids:
        seen = 0
        for asteroid in asteroids:
            if asteroid == start_asteroid:
                continue
            if asteroid_is_visible(grid, start_asteroid, asteroid):
                seen += 1
        if seen > max_seen:
            max_seen = seen
            max_seen_point = start_asteroid

    num_destroyed = 0
    last_destroyed = None
    # Basically: rotate by pi/2. add 2*pi if negative because atan2 has a range of (-pi-pi] which i dont like
    slopes = {key: (pi/2 + float(atan2(key[1] - max_seen_point[1], key[0] - max_seen_point[0])) + float(0 if pi/2 + float(atan2(key[1] - max_seen_point[1], key[0] - max_seen_point[0])) >= 0 else 2*pi)) % (pi*2)
              for key in grid if grid[key] and key != max_seen_point}
    current_laser = 0
    while num_destroyed < 200:
        # I changed it away from sympy but if slopes is a sympy thing it complains about being compared to float("inf"). sigh
        next_dist = ARBITRARY_CONSTANT_FOR_INFINITY
        next_thing = None
        for key in slopes:
            thing = slopes[key]
            t = thing - current_laser
            # It's gonna take a full round to get to this
            if t <= 0:
                thing += 2*pi
                t = thing - current_laser
            if t < next_dist:
                next_dist = t
                next_thing = thing
        next_to_destroy = next(
            slope for slope in slopes if slopes[slope] == next_thing and asteroid_is_visible(slopes, max_seen_point, slope))
        current_laser = slopes.pop(next_to_destroy)
        num_destroyed += 1

    return next_to_destroy[0] * 100 + next_to_destroy[1]


print(part_one(get_input()))
print(part_two(get_input()))

# print(get_input())
