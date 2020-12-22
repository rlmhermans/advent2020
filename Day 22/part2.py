deckone = [9, 2, 6, 3, 1]
decktwo = [5, 8, 4, 7, 10]
# deckone = [13, 25, 18, 6, 42, 8, 37, 27, 44, 38, 10, 28, 50, 5, 16, 47, 30, 29, 39, 21, 2, 4, 12, 35, 32]
# decktwo = [20, 14, 46, 34, 7, 26, 15, 43, 36, 49, 11, 23, 31, 48, 1, 19, 45, 22, 24, 40, 41, 17, 33, 9, 3]

def score(deck):
    points = 0
    deck.reverse()
    for i, n in enumerate(deck):
        points += (i + 1) * n
    return points

while deckone and decktwo: 
    numberone = deckone.pop(0)
    numbertwo = decktwo.pop(0)

    if numberone > numbertwo:
        deckone += [numberone, numbertwo]
    else:
        decktwo += [numbertwo, numberone]

points = 0
if deckone:
    points = score(deckone)

else:
    points = score(decktwo)

print(points)