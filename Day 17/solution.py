from itertools import product
import numpy as np

with open('input') as f:
    input = f.readlines()

active_cubes = []

for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == '#':
            active_cubes.append((x, y, 0, 0))

directions = list(product([-1, 0, 1], repeat=4))
directions.remove((0, 0, 0, 0))

STEPS = 6
start_width = len(line)

for step in range(1, STEPS + 1):
    depth = step + 1
    temp_cubes = []
    active_cubes = set(active_cubes)
    for w in range(0 - step, depth):
        for z in range(0 - step, depth):
            for y in range(0 - step, start_width + step):
                for x in range(0 - step, start_width + step):
                    neighbours = []

                    for direction in directions:
                        neighbours.append((x + direction[0], y + direction[1], z + direction[2], w + direction[3]))

                    active = (x, y, z, w) in active_cubes
                    active_neighbours = set(neighbours).intersection(active_cubes)
                    if active and 2 <= len(active_neighbours) <= 3 or not active and len(active_neighbours) == 3:
                        temp_cubes.append((x, y, z, w))

    active_cubes = temp_cubes   
    
print(len(active_cubes))