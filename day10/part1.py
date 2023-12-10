import sys
sys.path.append('../')
from parse_input import parse_input

input_grid = parse_input('input.txt', 'matrix')

#[ print(line) for line in input_grid ]

START_DIRECTIONS = [ (-1,0), (0, -1), (0, 1), (1, 0) ]

pipe_length = 0

def find_start(grid, char = 'S'):
    for y,line in enumerate(grid):
        if char in line:
            print(f'Start: {(y, line.index(char))}')
            return (y, line.index(char))

    return None

def follow_pipe(grid, pos, directions = START_DIRECTIONS, pipe_length = 1):
    # find exit
    directions = get_connections(grid, pos)

    if not directions: # with nowhere to go, we circled around to the start
        return pipe_length, None, None
    else:
        next_pos = directions[0]

        # mark as processed
        grid[pos[0]][pos[1]] = 's'

        # continue or return the length
        #if next_pos:
        #    return follow_pipe(grid, next_pos, directions, pipe_length + 1)

        return pipe_length, next_pos, directions

def get_connections(grid, pos):
    directions = []

    char = grid[pos[0]][pos[1]]

    #print(f'Checking {char} at {pos}')
    if char in '|LJS' and 0 < pos[0] and grid[pos[0]-1][pos[1]] in '|7F': # n
        directions.append((pos[0]-1,pos[1]))
    if char in '-J7S' and 0 < pos[1] and grid[pos[0]][pos[1]-1] in '-LF': # w
        directions.append((pos[0],pos[1]-1))
    if char in '-LFS' and pos[1] < len(grid) -1 and grid[pos[0]][pos[1]+1] in '-J7': # e
        directions.append((pos[0],pos[1]+1))
    if char in '|7FS' and pos[0] < len(grid) -1 and grid[pos[0]+1][pos[1]] in '|LJ': # s
        directions.append((pos[0]+1,pos[1]))

    return directions

def get_pipe_length():
    current_pos = find_start(input_grid)
    length = 1
    next_directions = START_DIRECTIONS

    while current_pos is not None:
        length, current_pos, next_directions = follow_pipe(input_grid, current_pos, next_directions, length)
        length += 1
        
    return length

print(get_pipe_length() // 2)

#    | is a vertical pipe connecting north and south.
#    - is a horizontal pipe connecting east and west.
#    L is a 90-degree bend connecting north and east.
#    J is a 90-degree bend connecting north and west.
#    7 is a 90-degree bend connecting south and west.
#    F is a 90-degree bend connecting south and east.
#    . is ground; there is no pipe in this tile.