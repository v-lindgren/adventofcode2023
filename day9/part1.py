import re
from numpy import diff
from functools import reduce
import sys
sys.path.append('../')
from parse_input import parse_input

input_lines = parse_input('input.txt', 'list')

histories = [ [ int(x) for x in re.split(' ', line) ] for line in input_lines ]

def expand_history(history):
    tmp_history = [ history.copy() ]

    i = 0
    while len(set(tmp_history[i])) > 1:
        tmp_history.append(list(diff(tmp_history[i])))
        i += 1


    return tmp_history

def add_next(history, depth = 0):
    if depth == len(history) - 1:
        history[depth].append(history[depth][0])
        return history[depth][0]
    else:
        history[depth].append(history[depth][-1] + add_next(history, depth +1))
        return history[depth][-1]


sum = 0
for history in histories:
    history = expand_history(history)
    add_next(history)
    sum += history[0][-1]

print(sum)