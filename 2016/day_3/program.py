def get_input():
    with open("day_3/input.txt") as f:
        file = f.read().splitlines()

    return file


def part_one(file):
    triangles = []
    for line in file:
        triangle = []
        line = line.strip()
        line = line.replace("   ", " ")
        line = line.replace("  ", " ")
        for num in line.split(" "):
            triangle.append(int(num))
        triangles.append(triangle)
    count_valid = 0
    for triangle in triangles:
        if triangle[0] + triangle[1] > triangle[2] and triangle[1] + triangle[2] > triangle[0] and triangle[2] + triangle[0] > triangle[1]:
            count_valid += 1

    return count_valid


def part_two(file):
    triangles = []
    for line in file:
        line = line.strip()
        line = line.replace("   ", " ")
        line = line.replace("  ", " ")
        for idx, num in enumerate(line.split(" ")):
            incomplete = [
                triangle for triangle in triangles if len(triangle[1]) < 3]
            broken = False
            for triangle in incomplete:
                if triangle[0] == idx:
                    triangle[1].append(int(num))
                    broken = True
                    break
            if not broken:
                triangles.append((idx, [int(num)]))
    count_valid = 0
    for triangle_pair in triangles:
        triangle = triangle_pair[1]
        if triangle[0] + triangle[1] > triangle[2] and triangle[1] + triangle[2] > triangle[0] and triangle[2] + triangle[0] > triangle[1]:
            count_valid += 1

    return count_valid


print(part_one(get_input()))
print(part_two(get_input()))
