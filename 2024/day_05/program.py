from collections import defaultdict


def get_input():
    with open("day_05/input.txt", "r") as f:
        contents = f.read()
        rules = defaultdict(list)
        for line in contents.split("\n\n")[0].split("\n"):
            rule = line.split("|")
            rules[int(rule[1])].append(int(rule[0]))

        updates = []
        for line in contents.split("\n\n")[1].split("\n"):
            if not line:
                break
            updates.append([int(x) for x in line.split(",")])
        return rules, updates


def part_one(rules, updates):
    total = 0
    for update in updates:
        valid = True
        for idx, num in enumerate(update):
            for num_rule in rules[num]:
                # Each number in the rules list must be before num
                if num_rule in update[idx:]:
                    valid = False
                    break
            if not valid:
                break
        else:
            total += update[len(update) // 2]
    return total


def part_two(rules, updates):
    total = 0
    for update in updates:
        ever_invalid = False
        valid = False
        while not valid:
            valid = True
            for idx, num in enumerate(update):
                for rule_num in rules[num]:
                    # Each number in the rules list must be BEFORE num
                    if rule_num in update[idx:]:
                        valid = False
                        ever_invalid = True
                        rule_num_idx = update.index(rule_num)
                        # Swap the two numbers
                        update[idx], update[rule_num_idx] = update[rule_num_idx], update[idx]
        if ever_invalid:
            total += update[len(update) // 2]
    return total


from functools import cmp_to_key


def alternative_with_sort(rules, updates):
    def sort_func(a, b):
        return -1 if a in rules[b] else 1 if b in rules[a] else 0

    total_part_one = 0
    total_part_two = 0
    for update in updates:
        new_update = sorted(update, key=cmp_to_key(sort_func))
        if new_update == update:
            total_part_one += update[len(update) // 2]
        else:
            total_part_two += new_update[len(update) // 2]
    print(total_part_one, total_part_two)


print(part_one(*get_input()))
print(part_two(*get_input()))
alternative_with_sort(*get_input())
