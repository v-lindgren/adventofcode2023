import re
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')

def get_numbers(numberlist):
    return [ int(y) for y in re.findall('[0-9]+', numberlist)]

all_winning_numbers = []

for line in input_lines:
    winning_numbers, my_numbers = map(get_numbers, re.split(':|\| +', line)[1::])

    my_winning_numbers = (set(winning_numbers) & set(my_numbers)) or {}
    all_winning_numbers.append(my_winning_numbers)

score = [ int(2 ** (len(x) - 1)) for x in all_winning_numbers]
print(sum(score))