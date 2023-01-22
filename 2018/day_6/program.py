
from collections import deque


def get_input():
    with open("day_6/input.txt", "r") as f:
        file = f.read().splitlines()

    points = []
    for line in file:
        points.append(tuple(map(int, line.split(","))))

    return points


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def floodfill_p1(orig_point, points):
    count_area = 0
    queue = deque([orig_point])
    visited = set()
    while queue:
        point = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_point = (point[0] + dx, point[1] + dy)
            if new_point not in visited and manhattan(new_point, orig_point) < min(manhattan(new_point, p) for p in points if p != orig_point):
                queue.append(new_point)
                visited.add(new_point)
                count_area += 1
                # If the new_point is receding from all of the other points it will go to infinity
                if all(manhattan(new_point, p) > manhattan(point, p) for p in points):
                    return -1

    return count_area


def floodfill_p2(start_point, points):
    count_area = 0
    queue = deque([start_point])
    visited = set()
    while queue:
        point = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_point = (point[0] + dx, point[1] + dy)
            if new_point not in visited and sum(manhattan(new_point, p) for p in points) < 10_000:
                queue.append(new_point)
                visited.add(new_point)
                count_area += 1

    return count_area


def part_one(points):
    areas = {point: 0 for point in points}
    for point in points:
        areas[point] = floodfill_p1(point, points)

    return max(areas.values())


def part_two(points):
    for start_x in range(-200, 200):
        for start_y in range(-200, 200):
            if sum(manhattan((start_x, start_y), p) for p in points) < 10_000:
                return floodfill_p2((start_x, start_y), points)


print(part_one(get_input()))
print(part_two(get_input()))
