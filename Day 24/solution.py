import re

with open('input') as f:
    input = f.readlines()

tiles = {}

for line in input:
    occurences = re.findall('(nw)|(ne)|(e)|(se)|(w)|(sw)', line)
    direction = {}
    for o in occurences:
        for group in o:
            if len(group) > 0:
                direction[group] = direction.get(group, 0) + 1

    n = direction.get('nw', 0) + direction.get('ne', 0)
    s = direction.get('sw', 0) + direction.get('se', 0)
    e = direction.get('se', 0) + direction.get('ne', 0) + \
        2 * direction.get('e', 0)
    w = direction.get('sw', 0) + direction.get('nw', 0) + \
        2 * direction.get('w', 0)

    tile = (n - s, e - w)
    tiles[tile] = tiles.get(tile, 0) + 1


blacks = [tile for tile in tiles if tiles[tile] % 2 != 0]
print('Part 1:', len(blacks))

DAYS = 100

directions = [(0, -2), (1, -1), (1, 1), (0, 2), (-1, 1), (-1, -1)]

for _ in range(DAYS):
    newblacks = []
    neighbours_of_blacks = {}
    for tile in blacks:
        neighbours = []
        for direction in directions:
            neighbours.append((tile[0] + direction[0], tile[1] + direction[1]))

        if 1 <= len(set(blacks) & set(neighbours)) <= 2:
            newblacks.append(tile)

        for neighbour in neighbours:
            neighbours_of_blacks[neighbour] = neighbours_of_blacks.get(neighbour, 0) + 1

    newblacks += [tile for tile in neighbours_of_blacks if neighbours_of_blacks[tile] == 2 and tile not in blacks]

    blacks = newblacks

print('Part 2:', len(blacks))