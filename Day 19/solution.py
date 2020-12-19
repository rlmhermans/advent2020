import regex as re

with open('input') as f:
    input = f.read().splitlines()

rules = {}
messages = []

for line in input:
    if ':' in line:
        parts = line.split(': ')
        rules[int(parts[0])] = parts[1]

    elif line:
        messages.append(line)

regex = rules[0]
while first_number := re.findall('\\d+|$', regex)[0]:
    regex = regex.replace(first_number, '(' + rules[int(first_number)] + ')', 1)

regex = regex.replace('("a")', 'a')
regex = regex.replace('("b")', 'b')
regex = regex.replace(' ', '')
print(regex)

print(len([line for line in input if re.fullmatch(regex, line)]))