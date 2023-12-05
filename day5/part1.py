import re
import sys
sys.path.append('../')
from parse_input import parse_input

input_groups = parse_input('input.txt', 'split list', '')

# First line is the seeds
seeds = [ int(x) for x in re.findall('[0-9]+', input_groups.pop(0)[0]) ]

def get_destination(maps, src_number):
    dst_number = src_number

    # Find the mapped number, defaulting to src number if not found
    for line in maps[0][1:]:
        dst_start, src_start, rng = [ int(x) for x in line.split() ]

        if src_start <= src_number < (src_start+rng):
            dst_number = dst_start + (src_number-src_start)

    # Call recursively if there's maps remaining
    return dst_number if len(maps) == 1 else get_destination(maps[1:], dst_number)

print(min([ get_destination(input_groups, seed) for seed in seeds ]))