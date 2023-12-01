import re
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')
total_sum = 0

for line in input_lines:
    number_dict = {'one': '1',
            'two': '2', 
            'three': '3', 
            'four': '4', 
            'five': '5', 
            'six': '6', 
            'seven': '7', 
            'eight': '8', 
            'nine': '9'}

    numbers = re.findall('[0-9]|one|two|three|four|five|six|seven|eight|nine', line)
    

    if len(numbers) > 0:
        if numbers[0] in number_dict:
            numbers[0] = number_dict.get(numbers[0])
        if numbers[-1] in number_dict:
            numbers[-1] = number_dict.get(numbers[-1])

        total_sum += int(numbers[0] + numbers[-1])

print(total_sum)