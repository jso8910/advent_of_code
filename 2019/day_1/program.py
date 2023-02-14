def get_input():
    with open("day_1/input.txt", "r") as f:
        return list(map(int, f.read().splitlines()))


def part_one(modules):
    def fuel_requirements(module): return module // 3 - 2
    return sum(map(fuel_requirements, modules))


def part_two(modules):
    def fuel_requirements(module):
        return (module // 3 - 2 + fuel_requirements(module // 3 - 2)) if module // 3 - 2 >= 0 else 0
    return sum(map(fuel_requirements, modules))


print(part_one(get_input()))
print(part_two(get_input()))
