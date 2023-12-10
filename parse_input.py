
def parse_input(file, outputtype = 'list', delimiter = None):
    inputlist = []
    with open(file, 'r') as input:
        for line in input:  
            inputlist.append(line.strip())
    
    match outputtype:
        case 'list':
            return inputlist
        case 'split list':
            if delimiter is not None:
                split_list = []
                
                group = []
                for line in inputlist:
                    if line == delimiter:
                        split_list.append(group)
                        group = []
                    else:
                        group.append(line)

                split_list.append(group) # append last group
                return split_list
            return None
        case 'matrix':
            inputmatrix = [ list(line) for line in inputlist ]
            return inputmatrix
        case _:
            return None