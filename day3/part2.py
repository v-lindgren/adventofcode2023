import re
from functools import reduce
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')
PART_SYMBOLS = '[*]'
gear_ratios = []

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
numbers_previous = []
numbers_current = []
numbers_next = []

for row_number, line in enumerate(input_lines):
    # find all numbers' locations in prev, current & next line
    numbers_current = numbers_next if numbers_next else get_part_number_positions(line)
    numbers_next = get_part_number_positions(input_lines[row_number + 1]) if row_number + 1 < len(input_lines) else []
    
    gear_positions = get_active_positions(line)

    active_pos = []
    if gear_positions:
        
        # create a sorted unique set of all nearby numbers' positions
        num_positions = numbers_previous + numbers_current + numbers_next
        
        for gear_pos in gear_positions:
            adjacent_numbers = []
            for num in num_positions:
                if gear_pos in range(num[1]-1, num[2]+1):
                    adjacent_numbers.append(int(num[0]))

            if len(adjacent_numbers) == 2:
                gear_ratios.append(reduce(lambda x,y: x*y, adjacent_numbers))
         
    numbers_previous = numbers_current

print(sum(gear_ratios))