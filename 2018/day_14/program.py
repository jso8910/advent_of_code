def get_input():
    with open("day_14/input.txt", "r") as f:
        return int(f.read())


def part_one(num_recipes):
    recipes = [3, 7]
    elf_one_recipe = 0
    elf_two_recipe = 1
    while len(recipes) < num_recipes + 10:
        sum_recipes = recipes[elf_one_recipe] + recipes[elf_two_recipe]
        if sum_recipes >= 10:
            recipes.append(sum_recipes // 10)
        recipes.append(sum_recipes % 10)
        elf_one_recipe += recipes[elf_one_recipe] + 1
        elf_two_recipe += recipes[elf_two_recipe] + 1

        elf_one_recipe %= len(recipes)
        elf_two_recipe %= len(recipes)

    return "".join(map(str, recipes[-10:]))


def part_two(last_recipes):
    last_recipes = str(last_recipes)
    recipes = "37"
    elf_one_recipe = 0
    elf_two_recipe = 1
    while recipes[-len(last_recipes):] != last_recipes and recipes[-len(last_recipes)-1:-1] != last_recipes:
        sum_recipes = int(recipes[elf_one_recipe]) + \
            int(recipes[elf_two_recipe])
        if sum_recipes >= 10:
            recipes += str(sum_recipes // 10)
        recipes += str(sum_recipes % 10)
        elf_one_recipe += int(recipes[elf_one_recipe]) + 1
        elf_two_recipe += int(recipes[elf_two_recipe]) + 1

        elf_one_recipe %= len(recipes)
        elf_two_recipe %= len(recipes)

    return recipes.index(last_recipes)


print(part_one(get_input()))
print(part_two(get_input()))
