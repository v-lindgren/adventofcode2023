import re
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')

sum_powers = 0

for line in input_lines:
    # find all '(count) (colour)' pairs
    matches = re.findall('[,;:] ([0-9]*) (\w+)', line)

    # sort by the the count (default sort sorts as string)
    matches.sort(key = lambda x:int(x[0]))

    # as we have sorted the sets from small to large, we can do this the
    # lazy way and just overwrite to end up with the largest value
    colour_count = { set[1]: int(set[0]) for set in matches }

    # multiply the values together, and add to sum
    power = 1
    for count in colour_count.values():
        power *= int(count)

    sum_powers += power

print(sum_powers)