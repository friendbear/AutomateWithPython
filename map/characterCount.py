# -*- coding: utf-8 -*-
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character.upper(), 0)
    count[character.upper()] = count[character.upper()] + 1

print(count)
# => {'I': 7, 'T': 6, ' ': 13, 'W': 2, 'A': 5, 'S': 3, 'B': 1, 'R': 5, 'G': 2, 'H': 3, 'C': 3, 'O': 2, 'L': 3, 'D': 3, 'Y': 1, 'N': 4, 'P': 1, ',': 1, 'E': 5, 'K': 2, '.': 1}

pprint.pprint(count)
