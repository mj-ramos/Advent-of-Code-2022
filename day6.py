def part(nr_dif):
    nr_c = 0
    pattern = ''
    for c in datastream:
        if len(pattern) == nr_dif:
            break
        else:
            if c not in pattern:
                pattern += c
            else:
                pattern = pattern[pattern.index(c)+1:] + c
            nr_c += 1    
    return nr_c

#------------------------------------------------------
with open('inputs/input6.txt') as f:
    datastream = f.read()

print(part(4),part(14)) #Right answers: 1640 