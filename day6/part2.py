import re
from functools import reduce
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')
time, record = [ int(reduce(lambda x, y: x + y, re.findall('[0-9]+', line))) for line in input_lines ]

# Start from the bottom and check for the lowest charging
# time that beats the record distance, the return the range
# of winning charging times
def get_winning(time, distance_to_beat):
    for charging_time in range(time):
        if charging_time * (time - charging_time) > distance_to_beat:
            return range(charging_time, (time - charging_time + 1))
    return None

print(len(get_winning(time, record)))