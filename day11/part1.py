import sys
sys.path.append('../')
from parse_input import parse_input

input_grid = parse_input('input.txt', 'matrix')

def expand_space(grid):
    # Don't make changes to the existing grid
    new_grid = [ line.copy() for line in grid ]
    
    # Add rows of space
    offset = 0 # each time we add items, the index of following shift up
    for index, line in enumerate(grid):
        if set(line) == set('.'):
            new_grid.insert(index + offset, line.copy())
            offset += 1

    # Add columns of space
    offset = 0 # each time we add items, the index of following shift up
    for index, value in enumerate(grid[0]):
        if set([ x[index] for x in grid]) == set('.'):
            [ x.insert(index + offset, '.') for x in new_grid ]
            offset += 1

    return new_grid

def find_galaxies(grid):
    galaxies = []
    for index_y, y in enumerate(grid):
        galaxies += [ (index_y, index_x) for index_x, x in enumerate(y) if x == '#' ]
    return galaxies

def find_distance(galaxies):
    total_distance = 0

    # we're comparing to a copy of the list, so we can remove elements
    # as we've measured them to all other
    galaxies_copy = galaxies.copy()

    for g_from in galaxies:
        # remove to make sure we only measure once
        galaxies_copy.remove(g_from)

        for g_to in galaxies_copy:
            diff = abs(g_to[0] - g_from[0]) + abs(g_to[1] - g_from[1])
            total_distance += diff

    return total_distance

new_grid = expand_space(input_grid)
galaxies = find_galaxies(new_grid)
print(find_distance(galaxies))