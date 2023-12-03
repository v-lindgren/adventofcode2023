import re
from functools import reduce
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')
PART_SYMBOLS = '[@/$%=*#+&\-]'
part_numbers = []

# numbers within 1 position of a part in the current
# or an adjecent line are part numbers
def get_active_positions(line):
    positions = []
    for match in re.finditer(PART_SYMBOLS, line):
        positions.append(match.start())

    return positions

def get_part_number_positions(line):
    positions =[]
    for match in re.finditer('[0-9]+', line):
        positions.append([match.group(), match.start(), match.end()])

    return positions

# We're looking at 3 lines at a time to check adjacency
parts_previous = []
parts_current = []
parts_next = []

for row_number, line in enumerate(input_lines):
    # find all part locations in prev, current & next line
    parts_current = parts_next if parts_next else get_active_positions(line)
    parts_next = get_active_positions(input_lines[row_number + 1]) if row_number + 1 < len(input_lines) else []

    # group positions of all parts
    active_positions = parts_previous + parts_current + parts_next
    active_positions.sort()

    # iterate over each number
    number_positions = get_part_number_positions(line)
    for number_pos in number_positions:

        # check if there's a symbol within 1 space
        for index in range(number_pos[1] - 1, number_pos[2] + 1):
            if index in active_positions:
                part_numbers.append(number_pos[0])
                break

    parts_previous = parts_current

print(sum([eval(num) for num in part_numbers]))
