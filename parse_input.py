
def parse_input(file, outputtype = 'list'):
    inputlist = []
    with open(file, 'r') as input:
        for line in input:  
            inputlist.append(line.strip())
    
    match outputtype:
        case 'list':
            return inputlist
        case _:
            return None