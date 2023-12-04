import re
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')

all_winning_numbers = []

for line in input_lines:
    number_groups = re.split(':|\| +', line)[1::]
    winning_numbers, my_numbers = map(
        lambda x: [ int(num) for num in re.findall('[0-9]+', x)],
        number_groups)

    my_winning_numbers = set(winning_numbers) & set(my_numbers)
    all_winning_numbers.append(my_winning_numbers)

score = [ int(2 ** (len(x) - 1)) for x in all_winning_numbers ]
print(sum(score))