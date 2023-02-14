import re
from math import lcm


def get_input():
    with open("day_12/input.txt", "r") as f:
        file = f.read().splitlines()

    prog = re.compile("<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")
    moons = []
    velocity = []
    for line in file:
        match = prog.match(line)
        x, y, z = map(int, match.groups())
        moons.append([x, y, z])
        velocity.append([0, 0, 0])

    return moons, velocity


def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def part_one(moons, velocity):
    for i in range(1000):
        for moon1 in zip(moons, velocity):
            for moon2 in zip(moons, velocity):
                moon1[1][0] += sign(moon2[0][0] - moon1[0][0])
                moon1[1][1] += sign(moon2[0][1] - moon1[0][1])
                moon1[1][2] += sign(moon2[0][2] - moon1[0][2])
        for moon in zip(moons, velocity):
            moon[0][0] += moon[1][0]
            moon[0][1] += moon[1][1]
            moon[0][2] += moon[1][2]
    return sum(sum(abs(x) for x in moon[0]) * sum(abs(x) for x in moon[1]) for moon in zip(moons, velocity))


def part_two(moons, velocity):
    i = 0
    x_vals = [[(moons[0][0], 0), (moons[1][0], 0),
               (moons[2][0], 0), (moons[3][0], 0)]]
    x_period = 0
    y_vals = [[(moons[0][1], 0), (moons[1][1], 0),
               (moons[2][1], 0), (moons[3][1], 0)]]
    y_period = 0
    z_vals = [[(moons[0][2], 0), (moons[1][2], 0),
               (moons[2][2], 0), (moons[3][2], 0)]]
    z_period = 0

    while True:
        i += 1
        for moon1 in zip(moons, velocity):
            for moon2 in zip(moons, velocity):
                if moon1 == moon2:
                    continue
                moon1[1][0] += sign(moon2[0][0] - moon1[0][0])
                moon1[1][1] += sign(moon2[0][1] - moon1[0][1])
                moon1[1][2] += sign(moon2[0][2] - moon1[0][2])
        for moon in zip(moons, velocity):
            moon[0][0] += moon[1][0]
            moon[0][1] += moon[1][1]
            moon[0][2] += moon[1][2]
        x_vals.append([(moon[0][0], moon[1][0])
                      for moon in zip(moons, velocity)])
        y_vals.append([(moon[0][1], moon[1][1])
                      for moon in zip(moons, velocity)])
        z_vals.append([(moon[0][2], moon[1][2])
                      for moon in zip(moons, velocity)])
        if x_vals[-1] == x_vals[0] and not x_period:
            x_period = len(x_vals) - 1
        if y_vals[-1] == y_vals[0] and not y_period:
            y_period = len(y_vals) - 1
        if z_vals[-1] == z_vals[0] and not z_period:
            z_period = len(z_vals) - 1
        if x_period and y_period and z_period:
            return lcm(x_period, y_period, z_period)

    # return sum(sum(abs(x) for x in moon[0]) * sum(abs(x) for x in moon[1]) for moon in zip(moons, velocity))


print(part_one(*get_input()))
print(part_two(*get_input()))
