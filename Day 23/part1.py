# cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
cups = [1, 5, 8, 9, 3, 7, 4, 6, 2]

current = 0
TIMES = 10000000
NROFCUPS = 1000000
for i in range(10, NROFCUPS + 1):
    cups.append(i)

for i in range(TIMES):
    if i % 1000 == 0: print(i)
    # print(f'-- move {i+1} --')
    # Set the current cup
    currentnumber = cups[current]

    # Take the next three
    next_three = []
    next_three_idxs = []
    for i in range(1, 4):
        idx = (current + i) % NROFCUPS
        next_three_idxs.append(idx)
        next_three.append(cups[idx])

    # cupstring = ' '.join([str(n) for n in cups])
    # print('cups: ', cupstring.replace(
    #     str(currentnumber), f'({str(currentnumber)})'))
    # print('pick up: ', next_three)

    # Destination is current cup number - 1
    destination = currentnumber - 1

    if destination < 1:
        destination = 9

    # Subtract 1 if the destination cup is among the three taken out
    while destination in next_three:
        destination -= 1
        if destination < 1:
            destination = 9

    originaldestidx = cups.index(destination)
    # print('destination: ', destination)

    # Remove the next three from circle
    for x in next_three:
        cups.remove(x)

    destidx = cups.index(destination)
    # Place the three cups back in the circle clockwise of the destination
    cups = cups[:destidx + 1] + next_three + cups[destidx + 1:]

    if destidx < current:
        underdesttindex = len(
            [x for x in next_three_idxs if x > originaldestidx])
        cups = cups[underdesttindex:] + cups[:underdesttindex]

    # Set next current to the cup clockwise of current
    current = (current + 1) % NROFCUPS

# Find the 1 and build a string starting clockwise of it
# print('-- final --')
idx = cups.index(1)
answer = cups[(idx + 1) % NROFCUPS] * cups[(idx + 2) % NROFCUPS]
print(answer)
