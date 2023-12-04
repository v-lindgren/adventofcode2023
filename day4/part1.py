import re
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')

all_winning_numbers = []

for line in input_lines:
    # Get the numbers from the line, then store as ints in two lists
    number_groups = re.split(':|\| +', line)[1::]
    winning_numbers, my_numbers = map(
        lambda x: [ int(num) for num in re.findall('[0-9]+', x)],
        number_groups)

    # Check for winning numbers
    my_winning_numbers = set(winning_numbers) & set(my_numbers)
    all_winning_numbers.append(my_winning_numbers)

# empty sets becomes 2^-1 = 0.5, but int conversion rounds to 0
score = [ int(2 ** (len(x) - 1)) for x in all_winning_numbers ]
print(sum(score))