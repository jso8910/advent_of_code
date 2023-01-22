from numpy import sign


def get_input():
    with open("day_20/input.txt", "r") as f:
        file = f.read().splitlines()

    particles = []
    for line in file:
        particle = list(map(int, line.split(", ")[0].split("=")[
                        1].strip("<>").split(",")))
        velocity = list(map(int, line.split(", ")[1].split("=")[
                        1].strip("<>").split(",")))
        acceleration = list(
            map(int, line.split(", ")[2].split("=")[1].strip("<>").split(",")))
        particles.append((particle, velocity, acceleration))

    return particles


def manhattan(particle):
    return abs(particle[0]) + abs(particle[1]) + abs(particle[2])


def accel_vector(particle_accel):
    return (particle_accel[0]**2 + particle_accel[1]**2 + particle_accel[2]**2)**0.5


def part_one(particles):
    # I'm gonna simulate it because, whatever
    tick = 0
    while True:
        tick += 1
        for particle in particles:
            # Update velocity
            particle[1][0] += particle[2][0]
            particle[1][1] += particle[2][1]
            particle[1][2] += particle[2][2]

            # Update particle position
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[0][2] += particle[1][2]

        # Don't run this too much
        if tick % 100 == 0:
            to_break = True
            min_dist = float("inf")
            min_dist_idx = None
            # Find the particle closest to 0,0,0
            for idx, particle in enumerate(particles):
                if manhattan(particle[0]) < min_dist:
                    min_dist = manhattan(particle[0])
                    min_dist_idx = idx

            # Find out if the particle will ever go past another in manhattan distance
            for particle in particles:
                if particle == particles[min_dist_idx]:
                    continue
                if accel_vector(particles[min_dist_idx][2]) > accel_vector(particle[2]):
                    to_break = False
                    break
            if to_break:
                break

    min_dist = float("inf")
    min_dist_idx = None
    for idx, particle in enumerate(particles):
        if manhattan(particle[0]) < min_dist:
            min_dist = manhattan(particle[0])
            min_dist_idx = idx

    return min_dist_idx


def part_two(particles: list[tuple[list[int]]]):
    # Yay, this one I actually have to simulate!
    tick = 0
    while True:
        tick += 1
        all_receding = True
        for particle in particles:
            initial_p = particle[0].copy()
            # Update velocity
            particle[1][0] += particle[2][0]
            particle[1][1] += particle[2][1]
            particle[1][2] += particle[2][2]

            # Update particle position
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[0][2] += particle[1][2]

            # Ok so essentially, unless there is a stupid input (Eric wouldn't do this to us), once they are all moving away,
            # They shouldn't collide
            if manhattan(particle[0]) < manhattan(initial_p):
                all_receding = False

        if all_receding:
            break
        to_rem = []
        for p1 in particles:
            for p2 in particles:
                if p1 == p2:
                    continue
                if p1[0] == p2[0]:
                    to_rem.append(p1)
                    to_rem.append(p2)

        for item in to_rem:
            try:
                particles.remove(item)
            except:
                # There was a duplicate from a 3+ particle collision
                pass

    return len(particles)


print(part_one(get_input()))
print(part_two(get_input()))
