import re
from functools import reduce
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')
times, records = [ [ int(time) for time in re.findall('[0-9]+', line) ] for line in input_lines ]

# Start from the bottom and check for the lowest charging
# time that beats the record distance, the return the range
# of winning charging times
def get_winning(time, distance_to_beat):
	for charging_time in range(time):
		if charging_time * (time - charging_time) > distance_to_beat:
			return range(charging_time, (time - charging_time + 1))
	return None

# Get the number of possible winning charging times for each race
solution_counts = [ len(get_winning(time, records[index])) for index, time in enumerate(times) ]

print(reduce(lambda x,y: x * y, solution_counts))