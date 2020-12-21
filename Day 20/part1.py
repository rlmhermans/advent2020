import re

def turn_right(image):
    newimage = []
    for i in range(len(image[0])):
        newline = ''
        for line in image:
            newline = line[i] + newline
        newimage.append(newline)
    return newimage

with open('sample') as f:
    input = f.read().split('\n\n')

edges = []
for line in input:
    image = line.split('\n')[1:]

    left = ''
    right = ''
    for d in image:
        left += d[0]
        right += d[-1]

    top = image[0]
    bottom = image[9]

    edges.append(top)
    edges.append(bottom)
    edges.append(left)
    edges.append(right)

# firstcorner = ""
for line in input:
    nr, image = line.split(':\n')
    image = image.split('\n')

    left = ''
    right = ''
    for d in image:
        left += d[0]
        right += d[-1]

    occurences = 0
    occurences += edges.count(image[0][::-1])
    occurences += edges.count(image[0])
    occurences += edges.count(image[9][::-1])
    occurences += edges.count(image[9])
    occurences += edges.count(left[::-1])
    occurences += edges.count(left)
    occurences += edges.count(right[::-1])
    occurences += edges.count(right)

    if not occurences > 6: corners[nr] = image


    # image.reverse()
    # image = turn_right(image)

# eerste corner ophalen, image (list) starten met die data, tiles passen, als match, toevoegen aan image. Lijn voor lijn, tot andere corner.