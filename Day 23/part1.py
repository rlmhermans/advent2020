MOVES = 10000000
NROFCUPS = 1000000
# MOVES = 10
# NROFCUPS = 9

# cups = [0, 2, 5, 8, 6, 4, 7, 3, 9, 1] # 389125467
# cups = [0, 2, 5, 8, 6, 4, 7, 10, 9, 1] + list(range(11, NROFCUPS + 1)) + [3] # 389125467
cups = [0, 5, 10, 7, 6, 8, 2, 4, 9, 3] + list(range(11, NROFCUPS + 1)) + [1] # 158937462

current = 1

for i in range(MOVES):
    destination = current - 1
    if destination < 1:
        destination = NROFCUPS

    next_three = [cups[current], cups[cups[current]], cups[cups[cups[current]]]]
    while destination in next_three:
        destination -= 1
        if destination < 1:
            destination = NROFCUPS

    cups[current] = cups[next_three[2]]
    cups[next_three[2]] = cups[destination]
    cups[destination] = next_three[0]
    current = cups[current]

answer = cups[1] * cups[cups[1]]
print(answer)