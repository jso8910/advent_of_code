from typing import List, Tuple, Dict
from collections import defaultdict
from collections import defaultdict, deque


def get_input():
    with open("day_13/input.txt", "r") as f:
        file = f.read().splitlines()

    grid = defaultdict(bool)
    carts = []
    for row_idx, row in enumerate(file):
        for col_idx, char in enumerate(row):
            if char:
                grid[col_idx + row_idx *
                     1j] = char if char in ["\\", "+", "/"] else True
            if char in "^>v<":
                match char:
                    case "^":
                        dir = -1j
                    case ">":
                        dir = 1
                    case "v":
                        dir = 1j
                    case "<":
                        dir = -1
                carts.append([col_idx + row_idx*1j, dir,
                             deque([turn_left, lambda x: x, turn_right])])

    return grid, carts


def turn_right(dir):
    match dir:
        case -1j:
            return 1
        case 1:
            return 1j
        case 1j:
            return -1
        case -1:
            return -1j


def turn_left(dir):
    match dir:
        case -1j:
            return -1
        case -1:
            return 1j
        case 1j:
            return 1
        case 1:
            return -1j


def part_one(grid, carts):
    while True:
        for cart in sorted(carts, key=lambda x: (x[0].imag, x[0].real)):
            current_point = grid[cart[0]]
            if current_point == True:
                cart[0] = cart[0] + cart[1]
            elif current_point == "/":
                if cart[1] == -1j:
                    cart[1] = 1
                elif cart[1] == 1j:
                    cart[1] = -1
                elif cart[1] == 1:
                    cart[1] = -1j
                elif cart[1] == -1:
                    cart[1] = 1j
                cart[0] = cart[0] + cart[1]
            elif current_point == "\\":
                if cart[1] == 1:
                    cart[1] = 1j
                elif cart[1] == -1:
                    cart[1] = -1j
                elif cart[1] == 1j:
                    cart[1] = 1
                elif cart[1] == -1j:
                    cart[1] = -1
                cart[0] = cart[0] + cart[1]
            elif current_point == "+":
                cart[1] = cart[2][0](cart[1])
                cart[2].rotate(-1)
                cart[0] = cart[0] + cart[1]
            if any(cart_1[0] == cart_2[0] for c1i, cart_1 in enumerate(carts) for c2i, cart_2 in enumerate(carts) if c1i != c2i):
                return [f"{int(cart_1[0].real)},{int(cart_1[0].imag)}" for cart_1 in carts for cart_2 in carts if cart_1 != cart_2 and cart_1[0] == cart_2[0]][0]


def part_two(grid, carts):
    crashed = []
    i = 0
    while True:
        for cart in sorted(carts, key=lambda x: (x[0].imag, x[0].real)):
            if cart in crashed:
                continue
            current_point = grid[cart[0]]
            if current_point == True:
                cart[0] = cart[0] + cart[1]
            elif current_point == "/":
                if cart[1] == -1j:
                    cart[1] = 1
                elif cart[1] == 1j:
                    cart[1] = -1
                elif cart[1] == 1:
                    cart[1] = -1j
                elif cart[1] == -1:
                    cart[1] = 1j
                cart[0] = cart[0] + cart[1]
            elif current_point == "\\":
                if cart[1] == 1:
                    cart[1] = 1j
                elif cart[1] == -1:
                    cart[1] = -1j
                elif cart[1] == 1j:
                    cart[1] = 1
                elif cart[1] == -1j:
                    cart[1] = -1
                cart[0] = cart[0] + cart[1]
            elif current_point == "+":
                cart[1] = cart[2][0](cart[1])
                cart[2].rotate(-1)
                cart[0] = cart[0] + cart[1]
            if any(cart_1[0] == cart_2[0] for c1i, cart_1 in enumerate(carts) for c2i, cart_2 in enumerate(carts) if c1i != c2i):
                [(crashed.append(cart_1), crashed.append(
                    cart_2)) for c1i, cart_1 in enumerate(carts) for c2i, cart_2 in enumerate(carts) if c1i != c2i and cart_1[0] == cart_2[0] and cart_1 not in crashed and cart_2 not in crashed]
        if len([c for c in carts if c not in crashed]) == 1:
            return f"{int([c for c in carts if c not in crashed][0][0].real)},{int([c for c in carts if c not in crashed][0][0].imag)}"


print(part_one(*get_input()))
print(part_two(*get_input()))
