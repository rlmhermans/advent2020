f = open('input')
input = f.readlines()[1]
parts = input.split(',')
lines_and_offsets = {}

for i, l in enumerate(parts):
    if l != 'x':
        lines_and_offsets[int(l)] = i

step = 1
current = 1

for line, offset in lines_and_offsets.items():
    while True:
        if (current + offset) % line == 0:
            break
        current += step
    step *= line

print(current)
