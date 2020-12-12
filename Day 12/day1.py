f = open('input')

boat_x = 0
boat_y = 0
waypoint_x = 10
waypoint_y = 1


def move_south(distance):
    global waypoint_y
    waypoint_y -= distance


def move_north(distance):
    global waypoint_y
    waypoint_y += distance


def move_west(distance):
    global waypoint_x
    waypoint_x -= distance


def move_east(distance):
    global waypoint_x
    waypoint_x += distance


def move_forward(times):
    global boat_x, boat_y, waypoint_x, waypoint_y
    boat_x += waypoint_y * times
    boat_y += waypoint_x * times


def counterclockwise(degrees):
    if degrees == 90:
        clockwise(270)
    elif degrees == 180:
        clockwise(180)
    elif degrees == 270:
        clockwise(90)


def clockwise(degrees):
    global boat_x, boat_y, waypoint_x, waypoint_y

    if degrees == 90:
        temp = -waypoint_x
        waypoint_x = waypoint_y
        waypoint_y = temp

    elif degrees == 180:
        for _ in range(2):
            clockwise(90)
    elif degrees == 270:
        for _ in range(3):
            clockwise(90)


commands = {
    'S': move_south,
    'N': move_north,
    'E': move_east,
    'W': move_west,
    'F': move_forward,
    'L': counterclockwise,
    'R': clockwise
}

for line in f:
    command = line[0]
    value = int(line[1:])

    commands[command](value)

print('Part 1: ', abs(boat_x) + abs(boat_y))
