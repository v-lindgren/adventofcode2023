import re
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')

def parse_instructions(lines):
    instructions = lines.pop(0)
    # create a dict on the format location: { L: left_destination, R: right_destination }
    locations = { loc: {'L': left, 'R': right } for loc, left, right in [ re.findall('[A-Z]+', line) for line in lines if line ] }
    return instructions, locations

instructions, locations = parse_instructions(input_lines)

# iterate through instructions
pos, DESTINATION = 'AAA', 'ZZZ'
i, steps = 0, 0
while True:
    pos = locations[pos][instructions[i]]
    steps += 1

    if pos == DESTINATION:
        break
    # if we've reached the end, start at 0 again
    i = (i + 1) % len(instructions)

print(steps)