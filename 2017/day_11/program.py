from collections import deque


def get_input():
    with open("day_11/input.txt", "r") as f:
        file = f.read()

    # INSTRUCTION_MAPS = {
    #     "N":  (0, 1, -1),
    #     "NE": (+1, point[1] + 0, point[2] - 1),
    #     "SE": (point[0] + 1, point[1] - 1, point[2] + 0),
    #     "S":  (point[0] + 0, point[1] - 1, point[2] + 1),
    #     "SW": (point[0] - 1, point[1] + 0, point[2] + 1),
    #     "NW": (point[0] - 1, point[1] + 1, point[2] + 0),
    # }

    return [instruction.upper() for instruction in file.split(",")]


def get_neighbors(point):
    # S N SE NE SW NW
    return {
        "N":  (point[0] + 0, point[1] + 1, point[2] - 1),
        "NE": (point[0] + 1, point[1] + 0, point[2] - 1),
        "SE": (point[0] + 1, point[1] - 1, point[2] + 0),
        "S":  (point[0] + 0, point[1] - 1, point[2] + 1),
        "SW": (point[0] - 1, point[1] + 0, point[2] + 1),
        "NW": (point[0] - 1, point[1] + 1, point[2] + 0),
    }
    # return {"S": point + 2j, "N": point - 2j, "SE": point + 1 + 1j, "NE": point + 1 - 1j, "SW": point - 1 + 1j, "NW": point - 1 - 1j}


def part_one(directions):
    end_point = (0, 0, 0)
    for direction in directions:
        end_point = get_neighbors(end_point)[direction]

    return sum(map(abs, end_point)) // 2


def part_two(directions):
    max_dist = 0
    end_point = (0, 0, 0)
    for direction in directions:
        end_point = get_neighbors(end_point)[direction]
        max_dist = max(max_dist, sum(map(abs, end_point)) // 2)

    return max_dist


print(part_one(get_input()))
print(part_two(get_input()))
