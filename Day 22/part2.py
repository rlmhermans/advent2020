# deckone = [9, 2, 6, 3, 1]
# decktwo = [5, 8, 4, 7, 10]
deckone = [13, 25, 18, 6, 42, 8, 37, 27, 44, 38, 10, 28, 50, 5, 16, 47, 30, 29, 39, 21, 2, 4, 12, 35, 32]
decktwo = [20, 14, 46, 34, 7, 26, 15, 43, 36, 49, 11, 23, 31, 48, 1, 19, 45, 22, 24, 40, 41, 17, 33, 9, 3]

def score(deck):
    points = 0
    deck.reverse()
    for i, n in enumerate(deck):
        points += (i + 1) * n
    return points

def game(deckone, decktwo):
    previousconfig = set()
    while deckone and decktwo:
        configone = ','.join([str(i) for i in deckone])
        configtwo = ','.join([str(i) for i in decktwo])
        config = configone + ';' + configtwo
        if not config in previousconfig:
            previousconfig.add(config)
            numberone = deckone.pop(0)
            numbertwo = decktwo.pop(0)

            winner = 0
            if len(deckone) >= numberone and len(decktwo) >= numbertwo:
                winner = game(deckone[:numberone], decktwo[:numbertwo])
                
            elif numberone > numbertwo:
                winner = 1
            
            if winner:
                deckone += [numberone, numbertwo]
            else:
                decktwo += [numbertwo, numberone]

            if not deckone:
                return 0
            if not decktwo:
                return 1
        else:
            return 1

winner = game(deckone, decktwo)

points = 0
if winner == 1:
    points = score(deckone)

else:
    points = score(decktwo)

print(points)