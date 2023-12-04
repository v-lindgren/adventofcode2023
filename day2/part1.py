import re
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')

max_possible = {
    'red': 12,
    'green': 13,
    'blue': 14
}

sum_ids = 0

for line in input_lines:
    # find all '(count) (colour)' pairs
    matches = re.findall('([0-9]+) ([A-z]+)', line)

    # sort by the count (default sort is by first char in string)
    matches.sort(key = lambda x:int(x[0]))

    # as we have sorted the sets from small to large, we can do this the
    # lazy way and just overwrite to end up with the largest value
    colour_count = { set[1]: int(set[0]) for set in matches }

    # if the count of all colours is lower than the maximum possible,
    # add the game's id to the sum
    if all(max_possible[colour] >= colour_count[colour] for colour in colour_count):
        sum_ids += int(re.findall('Game ([0-9]*)', line)[0])

print(sum_ids)