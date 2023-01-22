from numpy import sign
from heapq import nlargest


def get_input():
    with open("day_11/input.txt", "r") as f:
        return int(f.read())


def part_one(serial_number):
    grid = {}
    for y in range(1, 300+1):
        for x in range(1, 300+1):
            rack_id = x + 10
            power = rack_id * y
            power += serial_number
            power *= rack_id
            # Get 100s digit
            power = int(str(power)[-3])
            power -= 5
            grid[x + y*1j] = power

    max_power = -1
    max_power_coord = None
    for start_y in range(1, 300+1 - 2):
        for start_x in range(1, 300+1 - 2):
            power = sum(grid[start_x+dx + (start_y+dy)*1j]
                        for dx in range(3) for dy in range(3))
            if power > max_power:
                max_power = power
                max_power_coord = (start_x, start_y)

    return f"{max_power_coord[0]},{max_power_coord[1]}"


def part_two(serial_number):
    grid = {}
    for y in range(1, 300+1):
        for x in range(1, 300+1):
            rack_id = x + 10
            power = rack_id * y
            power += serial_number
            power *= rack_id
            # Get 100s digit
            power = int(str(power)[-3])
            power -= 5
            grid[x + y*1j] = power

    max_power = -1
    max_power_coord = None
    prev_10_largest = 0
    for size in range(1, 300+1):
        powers = []
        for start_y in range(1, 300+1 - (size - 1)):
            for start_x in range(1, 300+1 - (size - 1)):
                power = sum(grid[start_x+dx + (start_y+dy)*1j]
                            for dx in range(size) for dy in range(size))
                powers.append(power)
                if power > max_power:
                    max_power = power
                    max_power_coord = (start_x, start_y, size)

        ten_largest = sum(nlargest(10, powers))
        if ten_largest + 40 < prev_10_largest:
            break
        prev_10_largest = ten_largest

    return f"{max_power_coord[0]},{max_power_coord[1]},{max_power_coord[2]}"


print(part_one(get_input()))
print(part_two(get_input()))
