import re

def create_rule(line):
    name = line[:line.index(':')]
    nums = list(map(int, re.findall('[0-9]+', line)))
    check = lambda x : nums[0] <= x <= nums[1] or nums[2] <= x <= nums[3]
    return name, check

f = open('input')
input = f.readlines()
rules = []
valid_lines = []

for line in input:
    if 'or' in line:
        rules.append(create_rule(line))

    if ',' in line:
        line_valid = True

        for value in line.split(','):
            as_int = int(value)

            one_rule_valid = False
            for name, rule in rules:
                if rule(as_int):
                    one_rule_valid = True
            
            line_valid = line_valid and one_rule_valid

        if line_valid:
            nums = list(map(int, re.findall('[0-9]+', line)))
            valid_lines.append(nums)

line_length = len(valid_lines[0])
number_of_lines = len(valid_lines)
possibilities = {}

for name, rule in rules:
    for i in range(line_length):
        valid_for_all_lines = True


        for line in valid_lines:
            valid_for_all_lines = valid_for_all_lines and rule(int(line[i]))

        if valid_for_all_lines:
            poss = possibilities.get(name, [])
            poss.append(i)
            possibilities[name] = poss

print(possibilities) # And the rest can be done faster manually