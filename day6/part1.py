import re
from functools import reduce
import sys
sys.path.append('../')
from parse_input import parse_input

# Get times and distances for the races
input_lines = parse_input('input.txt', 'list')
times = [ int(time) for time in re.findall('[0-9]+', input_lines[0]) ]
records = [ int(record) for record in re.findall('[0-9]+', input_lines[1]) ]

# Start from the bottom and check for the lowest charging
# time that beats the record distance, the return the range
# of winning charging times
def get_winning(time, distance_to_beat):
	for charging_time in range(time):
		if charging_time * (time - charging_time) > distance_to_beat:
			return range(charging_time, (time - charging_time + 1))
	return None

# Get the number of possible charging times for each race
solution_counts = []
for index, time in enumerate(times):
    solution_counts.append(len(get_winning(time, records[index])))

print(reduce(lambda x,y: x * y, solution_counts))