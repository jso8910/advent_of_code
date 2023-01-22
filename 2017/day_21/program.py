from math import sqrt
import numpy as np


def get_input():
    with open("day_21/input.txt", "r") as f:
        file = f.read().splitlines()

    rules = []
    for line in file:
        start = line.split(" => ")[0]
        end = line.split(" => ")[1]
        start_arr = []
        end_arr = []
        for row in start.split("/"):
            start_arr.append([])
            # print(start_arr)
            for char in row:
                start_arr[-1].append(char == "#")

        for row in end.split("/"):
            end_arr.append([])
            for char in row:
                end_arr[-1].append(char == "#")

        for flip in gen_flips(np.array(start_arr)):
            if not any(np.array_equal(flip, x) for x in [r[0] for r in rules]):
                rules.append((flip, np.array(end_arr)))

    return rules


def gen_flips(pattern: np.array):
    flips = []
    for rotation in [0, 1, 2, 3]:
        new_state = np.rot90(np.copy(pattern), rotation)
        for flip_axis in (0, 1, 10):
            newer_state = new_state
            if flip_axis != 10:
                newer_state = np.flip(new_state, flip_axis)
            flips.append(newer_state)
    return flips


def gen_chunks(arr: np.array, N):
    A = []
    for v in np.vsplit(arr, arr.shape[0] // N):
        A.extend([*np.hsplit(v, arr.shape[0] // N)])
    return np.array(A)


def part_one(rules):
    state = np.array([
        [False, True, False],
        [False, False, True],
        [True, True, True],
    ])
    for i in range(5):
        size = state.shape[0]
        sub_state_size = 2 if size % 2 == 0 else 3
        chunks = list(gen_chunks(state, sub_state_size))
        for idx, chunk in enumerate(chunks):
            for rule in rules:
                if np.array_equal(chunk, rule[0]):
                    chunks[idx] = rule[1]
                    break
        num_per_row = int(sqrt(len(chunks)))
        state = np.concatenate([np.concatenate(chunks[n:n+num_per_row], axis=1)
                               for n in range(0, len(chunks), num_per_row)], axis=0)

    return state.sum()


def part_two(rules):
    state = np.array([
        [False, True, False],
        [False, False, True],
        [True, True, True],
    ])
    for i in range(18):
        print(i)
        size = state.shape[0]
        sub_state_size = 2 if size % 2 == 0 else 3
        chunks = list(gen_chunks(state, sub_state_size))
        for idx, chunk in enumerate(chunks):
            for rule in rules:
                if np.array_equal(chunk, rule[0]):
                    chunks[idx] = rule[1]
                    break
        num_per_row = int(sqrt(len(chunks)))
        state = np.concatenate([np.concatenate(chunks[n:n+num_per_row], axis=1)
                               for n in range(0, len(chunks), num_per_row)], axis=0)

    return state.sum()


print(part_one(get_input()))
print(part_two(get_input()))
