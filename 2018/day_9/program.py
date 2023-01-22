from collections import deque


def get_input():
    with open("day_9/input.txt", "r") as f:
        file = f.read()

    return int(file.split(" ")[0]), int(file.split(" ")[-2])


def part_one(num_players, final_marble):
    marbles = deque([0])
    players = deque([0 for _ in range(num_players)])
    for marble in range(1, final_marble + 1):
        if marble % 23 != 0:
            marbles.rotate(-2)
            marbles.appendleft(marble)
        else:
            marbles.rotate(7)
            players[0] += marbles.popleft() + marble
        players.rotate(1)

    return max(players)


def part_two(num_players, final_marble):
    final_marble *= 100
    marbles = deque([0])
    players = deque([0 for _ in range(num_players)])
    for marble in range(1, final_marble + 1):
        if marble % 23 != 0:
            marbles.rotate(-2)
            marbles.appendleft(marble)
        else:
            marbles.rotate(7)
            players[0] += marbles.popleft() + marble
        players.rotate(1)

    return max(players)


print(part_one(*get_input()))
print(part_two(*get_input()))
