from itertools import product


def get_input():
    with open("day_25/input.txt", "r") as f:
        file = f.read().splitlines()

    points = []
    for line in file:
        points.append(tuple(map(int, line.split(","))))

    return points


def manhattan(p1, p2):
    return sum(abs(p2[i] - p1[i]) for i in range(len(p1)))


class Point:
    def __init__(self, coord):
        self.coord = coord
        self.neighbors = []

    def __repr__(self):
        return str(self.coord)


class Points:
    def __init__(self, points):
        self.points: list[Point] = [Point(point) for point in points]

    def find_neighbors(self, p_idx):
        point: Point = self.points[p_idx]
        for p in self.points:
            if manhattan(point.coord, p.coord) <= 3:
                point.neighbors.append(p)


def part_one(points):
    points = Points(points)
    for i in range(len(points.points)):
        points.find_neighbors(i)
        # print(points.points[i].neighbors + [points.points[i]])

    constellations_old = [set(p.neighbors) | set([p])
                          for p in points.points]
    constellations = []
    for c in list(constellations_old):
        for c1 in list(constellations_old):
            if c1 == c:
                continue
            if c & c1:
                if c in constellations_old:
                    constellations_old.remove(c)
                # print(c)
                # print(c, c1)
                if c1 in constellations_old:
                    constellations_old.remove(c1)
                c = c | c1
                constellations_old.append(c)

    # I don't know why I need to do this twice but whatever
    values = set()
    for c in constellations_old:
        if values & c:
            constellations_old.remove(c)
        else:
            values |= c

    values = set()
    for c in constellations_old:
        if values & c:
            constellations_old.remove(c)
        else:
            values |= c
    return len(set(tuple(c) for c in constellations_old))


print(part_one(get_input()))
