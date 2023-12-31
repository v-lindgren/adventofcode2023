import re
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')

total_sum = 0

for line in input_lines:
    numbers = re.findall('[0-9]', line) # find all numbers
    total_sum += int(numbers[0] + numbers[-1]) # concatenate and add to sum

print(total_sum)