# Real input
from copy import deepcopy
IMMUNE_GROUPS_ORIGINAL = [
    {"units": 522,  "hp": 9327, "immune": [], "weak": [], "attack": {
        "type": "slashing", "damage": 177}, "initiative": 14, "type": "immune", "to_attack": None},
    {"units": 2801,  "hp": 3302, "immune": [], "weak": [], "attack": {
        "type": "bludgeoning", "damage": 10}, "initiative": 7, "type": "immune", "to_attack": None},
    {"units": 112,  "hp": 11322, "immune": [], "weak": [], "attack": {
        "type": "slashing", "damage": 809}, "initiative": 8, "type": "immune", "to_attack": None},
    {"units": 2974,  "hp": 9012, "immune": [], "weak": [], "attack": {
        "type": "slashing", "damage": 23}, "initiative": 11, "type": "immune", "to_attack": None},
    {"units": 4805,  "hp": 8717, "immune": [], "weak": ["radiation"], "attack": {
        "type": "bludgeoning", "damage": 15}, "initiative": 5, "type": "immune", "to_attack": None},
    {"units": 1466,  "hp": 2562, "immune": ["radiation", "fire"], "weak": [], "attack": {
        "type": "radiation", "damage": 17}, "initiative": 10, "type": "immune", "to_attack": None},
    {"units": 2513,  "hp": 1251, "immune": ["cold"], "weak": ["fire"], "attack": {
        "type": "slashing", "damage": 4}, "initiative": 3, "type": "immune", "to_attack": None},
    {"units": 6333,  "hp": 9557, "immune": ["slashing"], "weak": [], "attack": {
        "type": "fire", "damage": 14}, "initiative": 9, "type": "immune", "to_attack": None},
    {"units": 2582,  "hp": 1539, "immune": ["bludgeoning"], "weak": [], "attack": {
        "type": "slashing", "damage": 5}, "initiative": 2, "type": "immune", "to_attack": None},
    {"units": 2508,  "hp": 8154, "immune": [], "weak": ["bludgeoning", "cold"], "attack": {
        "type": "bludgeoning", "damage": 27}, "initiative": 4, "type": "immune", "to_attack": None},
]

INFECTION_GROUPS_ORIGINAL = [
    {"units": 2766,  "hp": 20953, "immune": [], "weak": ["fire"], "attack": {
        "type": "radiation", "damage": 14}, "initiative": 1, "type": "infection", "to_attack": None},
    {"units": 4633,  "hp": 18565, "immune": ["cold", "slashing"], "weak": [], "attack": {
        "type": "fire", "damage": 6}, "initiative": 15, "type": "infection", "to_attack": None},
    {"units": 239,  "hp": 47909, "immune": [], "weak": ["slashing", "cold"], "attack": {
        "type": "slashing", "damage": 320}, "initiative": 16, "type": "infection", "to_attack": None},
    {"units": 409,  "hp": 50778, "immune": ["radiation"], "weak": [], "attack": {
        "type": "fire", "damage": 226}, "initiative": 17, "type": "infection", "to_attack": None},
    {"units": 1280,  "hp": 54232, "immune": ["slashing", "fire", "bludgeoning"], "weak": [], "attack": {
        "type": "bludgeoning", "damage": 60}, "initiative": 13, "type": "infection", "to_attack": None},
    {"units": 451,  "hp": 38251, "immune": ["bludgeoning"], "weak": [], "attack": {
        "type": "bludgeoning", "damage": 163}, "initiative": 6, "type": "infection", "to_attack": None},
    {"units": 1987,  "hp": 37058, "immune": [], "weak": [], "attack": {
        "type": "slashing", "damage": 31}, "initiative": 20, "type": "infection", "to_attack": None},
    {"units": 1183,  "hp": 19147, "immune": [], "weak": ["slashing"], "attack": {
        "type": "fire", "damage": 24}, "initiative": 12, "type": "infection", "to_attack": None},
    {"units": 133,  "hp": 22945, "immune": ["cold", "bludgeoning"], "weak": ["slashing"], "attack": {
        "type": "radiation", "damage": 287}, "initiative": 19, "type": "infection", "to_attack": None},
    {"units": 908,  "hp": 47778, "immune": [], "weak": [], "attack": {
        "type": "fire", "damage": 97}, "initiative": 18, "type": "infection", "to_attack": None},
]


# # EXAMPLE INPUT
# IMMUNE_GROUPS_ORIGNAL = [
#     {"units": 17,  "hp": 5390, "immune": [], "weak": ["radiation", "bludgeoning"], "attack": {
#         "type": "fire", "damage": 4507}, "initiative": 2, "type": "immune", "to_attack": None},
#     {"units": 989,  "hp": 1274, "immune": ["fire"], "weak": ["bludgeoning", "slashing"], "attack": {
#         "type": "slashing", "damage": 25}, "initiative": 3, "type": "immune", "to_attack": None},
# ]

# INFECTION_GROUPS_ORIGINAL = [
#     {"units": 801,  "hp": 4706, "immune": [], "weak": ["radiation"], "attack": {
#         "type": "bludgeoning", "damage": 116}, "initiative": 1, "type": "infection", "to_attack": None},
#     {"units": 4485,  "hp": 2961, "immune": ["radiation"], "weak": ["fire", "cold"], "attack": {
#         "type": "slashing", "damage": 12}, "initiative": 4, "type": "infection", "to_attack": None},
# ]


def part_one():
    INFECTION_GROUPS = deepcopy(INFECTION_GROUPS_ORIGINAL)
    IMMUNE_GROUPS = deepcopy(IMMUNE_GROUPS_ORIGINAL)
    while True:
        # Target selection phase
        units_in_order = sorted(IMMUNE_GROUPS + INFECTION_GROUPS, key=lambda x: (
            x["units"] * x["attack"]["damage"], x["initiative"]), reverse=True)
        for unit in units_in_order:
            if unit["units"] <= 0:
                continue
            enemy_units = IMMUNE_GROUPS if unit["type"] == "infection" else INFECTION_GROUPS

            effective_power = unit["units"] * unit["attack"]["damage"]
            highest_attack = 0
            highest_attack_unit = None
            for enemy in [e for e in enemy_units if e not in [u["to_attack"] for u in units_in_order]]:
                if enemy["units"] <= 0:
                    continue
                if unit["attack"]["type"] in enemy["immune"]:
                    continue
                elif unit["attack"]["type"] in enemy["weak"]:
                    attack_power = effective_power * 2
                else:
                    attack_power = effective_power
                if attack_power > highest_attack:
                    highest_attack = attack_power
                    highest_attack_unit = enemy
                elif attack_power == highest_attack and enemy["attack"]["damage"] * enemy["units"] > highest_attack_unit["attack"]["damage"] * highest_attack_unit["units"]:
                    highest_attack_unit = enemy
                elif attack_power == highest_attack and enemy["attack"]["damage"] * enemy["units"] == highest_attack_unit["attack"]["damage"] * highest_attack_unit["units"] and enemy["initiative"] > highest_attack_unit["initiative"]:
                    highest_attack_unit = enemy
            unit["to_attack"] = highest_attack_unit

        # Attacking phase
        units_in_order = sorted(
            IMMUNE_GROUPS + INFECTION_GROUPS, key=lambda x: x["initiative"], reverse=True)
        for unit in units_in_order:
            enemy = unit["to_attack"]
            unit["to_attack"] = None
            if unit["units"] <= 0:
                continue
            if not enemy:
                continue
            effective_power = unit["units"] * unit["attack"]["damage"]
            if unit["attack"]["type"] in enemy["weak"]:
                attack_power = effective_power * 2
            else:
                attack_power = effective_power

            units_to_kill = attack_power // enemy["hp"]
            enemy["units"] -= units_to_kill
            enemy["units"] = max(enemy["units"], 0)

        # Check win
        infection_lost = True
        for group in INFECTION_GROUPS:
            if group["units"] > 0:
                infection_lost = False
                break
        immune_lost = True
        for group in IMMUNE_GROUPS:
            if group["units"] > 0:
                immune_lost = False
                break
        if infection_lost:
            return sum(unit["units"] if unit["units"] > 0 else 0 for unit in IMMUNE_GROUPS)
        elif immune_lost:
            return sum(unit["units"] if unit["units"] > 0 else 0 for unit in INFECTION_GROUPS)


def part_two():
    boost = 2
    delta_boost = 2
    won_before = False
    ever_won = False
    while True:
        INFECTION_GROUPS = deepcopy(INFECTION_GROUPS_ORIGINAL)
        IMMUNE_GROUPS = deepcopy(IMMUNE_GROUPS_ORIGINAL)
        for unit in IMMUNE_GROUPS:
            unit["attack"]["damage"] += boost
        while True:
            units_in_order = sorted(IMMUNE_GROUPS + INFECTION_GROUPS, key=lambda x: (
                x["units"] * x["attack"]["damage"], x["initiative"]), reverse=True)
            for unit in units_in_order:
                if unit["units"] <= 0:
                    continue
                enemy_units = IMMUNE_GROUPS if unit["type"] == "infection" else INFECTION_GROUPS

                effective_power = unit["units"] * unit["attack"]["damage"]
                highest_attack = 0
                highest_attack_unit = None
                for enemy in [e for e in enemy_units if e not in [u["to_attack"] for u in units_in_order]]:
                    if enemy["units"] <= 0:
                        continue
                    if unit["attack"]["type"] in enemy["immune"]:
                        continue
                    elif unit["attack"]["type"] in enemy["weak"]:
                        attack_power = effective_power * 2
                    else:
                        attack_power = effective_power
                    if attack_power > highest_attack:
                        highest_attack = attack_power
                        highest_attack_unit = enemy
                    elif attack_power == highest_attack and enemy["attack"]["damage"] * enemy["units"] > highest_attack_unit["attack"]["damage"] * highest_attack_unit["units"]:
                        highest_attack_unit = enemy
                    elif attack_power == highest_attack and enemy["attack"]["damage"] * enemy["units"] == highest_attack_unit["attack"]["damage"] * highest_attack_unit["units"] and enemy["initiative"] > highest_attack_unit["initiative"]:
                        highest_attack_unit = enemy
                unit["to_attack"] = highest_attack_unit

            # Attacking phase
            any_damage = False
            units_in_order = sorted(
                IMMUNE_GROUPS + INFECTION_GROUPS, key=lambda x: x["initiative"], reverse=True)
            for unit in units_in_order:
                enemy = unit["to_attack"]
                unit["to_attack"] = None
                if unit["units"] <= 0:
                    continue
                if not enemy:
                    continue
                effective_power = unit["units"] * unit["attack"]["damage"]
                if unit["attack"]["type"] in enemy["weak"]:
                    attack_power = effective_power * 2
                else:
                    attack_power = effective_power

                units_to_kill = attack_power // enemy["hp"]
                if units_to_kill > 0:
                    any_damage = True
                enemy["units"] -= units_to_kill
                enemy["units"] = max(enemy["units"], 0)
            if not any_damage:
                boost += 1
                won_before = False
                delta_boost = 1
                break
            # Check win
            infection_lost = True
            for group in INFECTION_GROUPS:
                if group["units"] > 0:
                    infection_lost = False
                    break
            immune_lost = True
            for group in IMMUNE_GROUPS:
                if group["units"] > 0:
                    immune_lost = False
                    break
            if infection_lost:
                # print("a", boost)
                if ever_won and not won_before and delta_boost == 1:
                    return sum(unit["units"] if unit["units"] > 0 else 0 for unit in IMMUNE_GROUPS)
                old_boost = boost
                boost //= 1.2
                boost = int(boost)
                delta_boost = old_boost - boost
                won_before = True
                ever_won = True
            elif immune_lost:
                # print("h")
                if not ever_won:
                    old_boost = boost
                    boost *= 2
                    delta_boost = old_boost - boost
                    won_before = False
                else:
                    old_boost = boost
                    boost += 1
                    delta_boost = old_boost - boost
                    won_before = False
                break


print(part_one())
print(part_two())
