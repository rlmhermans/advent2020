input = [17, 1, 3, 16, 19, 0]
END = 30000000

timestamped = {}
for i, x in enumerate(input):
    timestamped[x] = [i + 1]

start = len(input) + 1
previous = input[len(input) - 1]
previous_idxs = timestamped[previous]

for current in range(start, END + 1):
    new_number = max(previous_idxs) - min(previous_idxs)
    idxs = timestamped.get(new_number, [])
    idxs = [idxs.pop(), current] if len(idxs) > 0 else [current]
    timestamped[new_number] = idxs

    previous = new_number
    previous_idxs = idxs

print(new_number)