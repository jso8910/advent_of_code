from collections import defaultdict
from math import ceil


def get_input():
    with open("day_14/input.txt", "r") as f:
        file = f.read().splitlines()

    recipes = []
    for thing in file:
        recipe = {}
        recipe["ingredients"] = []
        recipe["result"] = {}
        ingredients, res = thing.split(" => ")
        for ingredient in ingredients.split(", "):
            recipe["ingredients"].append(
                {"quantity": int(ingredient.split(" ")[0]), "item": ingredient.split(" ")[1]})
        recipe["result"] = {"quantity": int(
            res.split(" ")[0]), "item": res.split(" ")[1]}
        recipes.append(recipe)

    return recipes


def num_required_to_make(recipes, n, res, ingredient, reserves):
    recipe = [recipe for recipe in recipes if recipe["result"]["item"] == res][0]
    num_recipes_to_make = ceil(n / recipe["result"]["quantity"])
    reserves[res] += num_recipes_to_make * recipe["result"]["quantity"]
    for i in recipe["ingredients"]:
        reserves[i["item"]] -= num_recipes_to_make * i["quantity"]
    return sum(num_required_to_make(
        recipes,
        # This represents the shortage of the item because I already subtracted. That's how many I need to make
        -reserves[i["item"]],
        i["item"],
        ingredient,
        reserves) if i["item"] != ingredient else i["quantity"]*num_recipes_to_make for i in recipe["ingredients"])


def part_one(recipes):
    reserves = defaultdict(int)
    return num_required_to_make(recipes, 1, "FUEL", "ORE", reserves)


def part_two(recipes):
    size_of_search = 1_000_000_000_000 // 200000
    i = 1_000_000_000_000 // 100000
    while True:
        reserves = defaultdict(int)
        num_used = num_required_to_make(recipes, i, "FUEL", "ORE", reserves)
        if num_used > 1_000_000_000_000:
            i -= size_of_search
            size_of_search //= 2
            size_of_search = max(size_of_search, 1)
        elif num_used < 1_000_000_000_000:
            reserves = defaultdict(int)
            if num_required_to_make(recipes, i + 1, "FUEL", "ORE", reserves) > 1_000_000_000_000:
                return i
            i += size_of_search
            size_of_search //= 2
            size_of_search = max(size_of_search, 1)


print(part_one(get_input()))
print(part_two(get_input()))
