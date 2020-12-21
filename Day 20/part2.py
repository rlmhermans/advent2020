import re

def turn_right(image):
    newimage = []
    for i in range(len(image[0])):
        newline = ''
        for line in image:
            newline = line[i] + newline
        newimage.append(newline)
    return newimage

def side_edges(image):
    left = ''
    right = ''
    for line in image:
        left += line[0]
        right += line[-1]

    return left,right

with open('input') as f:
    input = f.read().split('\n\n')

images = {}
edges = []
for line in input:
    nr, image = line.split(':\n')
    image = image.split('\n')

    images[nr] = []

    for _ in range(2):
        for _ in range(4):
            images[nr].append(image)
            image = turn_right(image)
        image.reverse()
        
    left, currentright = side_edges(image)
    top, bottom = image[0], image[9]

    edges.append(top)
    edges.append(top[::-1])
    edges.append(bottom)
    edges.append(bottom[::-1])
    edges.append(left)
    edges.append(left[::-1])
    edges.append(currentright)
    edges.append(currentright[::-1])

topleft = []
delete = 0
for nr in images:
    for image in images[nr]:
        if not len(topleft):
            top = image[0]
            left, _ = side_edges(image)

            if edges.count(top) + edges.count(left) == 2:
                topleft = image
                delete = nr

images.pop(delete)

bigimage = [[topleft]]
current = topleft

while edges.count(current[9]) > 1:
    delete = 0
    for nr in images:
        for image in images[nr]:
            if not delete:
                if image[0] == current[9]:
                    current = image
                    bigimage.append([image])
                    delete = nr
    images.pop(delete)

for line in bigimage:
    current = line[0]
    _, currentright = side_edges(current)
    while edges.count(currentright) > 1:
        delete = 0
        for nr in images:
            for image in images[nr]:
                if not delete:
                    nextleft, nextright = side_edges(image)
                    if nextleft == currentright:
                        current = image
                        currentright = nextright
                        line.append(image)
                        delete = nr
        images.pop(delete)

composedimage = []
for line in bigimage:
    for i in range(1, 9):
        fullline = ''
        for tile in line:
            fullline += tile[i][1:-1]
        composedimage.append(fullline)

skip = len(composedimage[0]) - 19
for _ in range(2):
    for _ in range(4):
        image_one_line = ''.join(composedimage)
        monsters = len(re.findall('#[#.]{' + str(skip) + '}#([#.]{4}##){3}#[#.]{' + str(skip) + '}#([#.]{2}#){5}', image_one_line))
        if monsters > 0:
            print(image_one_line.count('#')-monsters * 15)
        composedimage = turn_right(composedimage)
    composedimage.reverse()