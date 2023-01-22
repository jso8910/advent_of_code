import re


def get_input():
    with open("day_10/input.txt", "r") as f:
        file = f.read().splitlines()

    prog = re.compile(
        "position=<\s*(-?\d+),\s*(-?\d+)>\s*velocity=<\s*(-?\d+),\s*(-?\d+)>")

    points = []
    for line in file:
        match = re.match(prog, line)
        points.append({"loc": (int(match.group(1)), int(match.group(2))),
                      "velo": (int(match.group(3)), int(match.group(4)))})

    return points


def bounding_box(points):
    x_coordinates, y_coordinates = zip(*[p["loc"] for p in points])

    return [(min(x_coordinates), min(y_coordinates)), (max(x_coordinates), max(y_coordinates))]


def print_points(points):
    bbox = bounding_box(points)
    point_coords = [p["loc"] for p in points]
    for y in range(bbox[0][1], bbox[1][1] + 1):
        for x in range(bbox[0][0], bbox[1][0] + 1):
            if (x, y) in point_coords:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def part_one(points):
    min_bounding_box = float("inf")
    secs = 0
    while True:
        secs += 1
        for point in points:
            point["loc"] = (point["loc"][0] + point["velo"][0],
                            point["loc"][1] + point["velo"][1])
        bbox = bounding_box(points)
        bbox_size = abs((bbox[1][0] - bbox[0][0])*(bbox[1][1] - bbox[0][1]))
        if bbox_size < min_bounding_box:
            min_bounding_box = bbox_size
            # print(bbox_size, secs)
            if bbox_size < 800:
                print_points(points)
                return


def part_two(points):
    min_bounding_box = float("inf")
    secs = 0
    while True:
        secs += 1
        for point in points:
            point["loc"] = (point["loc"][0] + point["velo"][0],
                            point["loc"][1] + point["velo"][1])
        bbox = bounding_box(points)
        bbox_size = abs((bbox[1][0] - bbox[0][0])*(bbox[1][1] - bbox[0][1]))
        if bbox_size < min_bounding_box:
            min_bounding_box = bbox_size
            # print(bbox_size, secs)
            if bbox_size < 800:
                return secs


print(part_one(get_input()))
print(part_two(get_input()))
