def get_input():
    with open("day_3/input.txt") as f:
        # return [tuple(map(int, line.replace("   ", " ").replace("  ", " ").split("  "))) for line in f]
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
            # print(incomplete, num, idx)
            # for triangle in [triangle for triangle in triangles if len(triangle) < 3]:
            #     if triangle[0] // 100 == int(num) // 100:
            #         triangle.append(int(num))
            #         break
            broken = False
            for triangle in incomplete:
                if triangle[0] == idx:
                    triangle[1].append(int(num))
                    broken = True
                    break
            if not broken:
                triangles.append((idx, [int(num)]))
    # triangles = set(triangles)
    # print(triangles)
    count_valid = 0
    for triangle_pair in triangles:
        triangle = triangle_pair[1]
        # print(triangle, triangle[0] + triangle[1],
        #       triangle[1] + triangle[2], triangle[0] + triangle[2])
        if triangle[0] + triangle[1] > triangle[2] and triangle[1] + triangle[2] > triangle[0] and triangle[2] + triangle[0] > triangle[1]:
            count_valid += 1

    return count_valid


print(part_one(get_input()))
print(part_two(get_input()))
