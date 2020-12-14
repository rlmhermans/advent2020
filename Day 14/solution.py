import re
from itertools import product

PLACEHOLDER = 'X'
MASKSIZE = 36

f = open('input')
input = f.readlines()
mem = {}

for line in input:
    if 'mask' in line:
        masks = []
        line = line.replace('mask = ', '').strip()
        seq = list(line)

        indices = [i for i, c in enumerate(seq) if c == PLACEHOLDER]

        for t in product('12', repeat=len(indices)):
            for i, c in zip(indices, t):
                seq[i] = c
            masks.append(''.join(seq))

    if 'mem' in line:
        parts = re.findall('[0-9]+', line)
        value = int(parts[1])
        address = int(parts[0])
        binary_address = format(address, 'b')
        binary_address = '0' * (MASKSIZE - len(binary_address)) + binary_address

        for mask in masks:
            address_copy = list(binary_address)
            for i, _ in enumerate(binary_address):
                if mask[i] == '0':
                    continue
                if mask[i] == '1':
                    address_copy[i] = '1'
                if mask[i] == '2': 
                    address_copy[i] = '0'

            masked_address = ''.join(address_copy)
            mem[int(masked_address, 2)] = value

print(sum(mem.values()))
