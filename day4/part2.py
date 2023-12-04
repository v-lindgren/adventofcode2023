import re
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')

deck = list(input_lines)

# Parse a line(ticket) and return the count of winning numbers on it
def get_num_wins(line):
    number_groups = re.split(':|\| +', line)[1::]
    winning_numbers, my_numbers = map(
        lambda x: [ int(num) for num in re.findall('[0-9]+', x)],
        number_groups)
    
    return len(set(winning_numbers) & set(my_numbers))

# Create the original deck of cards, on the format 'index: [count, number_of_wins]'
deck = { i: [1, get_num_wins(x)] for i,x in enumerate(input_lines) }

for index, card in deck.items():
    # increase count of n following by number of current card
    for n in range(card[1]):
        deck[index+1 + n][0] += card[0]

print(sum([ x[0] for x in deck.values()]))