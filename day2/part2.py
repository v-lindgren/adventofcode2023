import re
from functools import reduce
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')

sum_powers = 0

for line in input_lines:
    # find all '(count) (colour)' pairs
    matches = re.findall('([0-9]+) ([A-z]+)', line)

    # sort by the the count (default sort is by first char in string)
    matches.sort(key = lambda x:int(x[0]))

    # as we have sorted the sets from small to large, we can do this the lazy
    # way and just overwrite to end up with the largest value for each colour
    colour_count = { set[1]: int(set[0]) for set in matches }

    # multiply the values together and add to sum
    power = reduce(lambda x,y: x * y, colour_count.values())
    sum_powers += power

print(sum_powers)