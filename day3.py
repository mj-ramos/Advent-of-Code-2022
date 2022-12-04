def readfile(file_name):
    with open(file_name) as f:
        return f.readlines()

def part_one():
    sum_priorities = 0

    for line in lines:
        items = [x for x in line[:-1]]
        if len(items)!=0:
            rucksack1 = items[:len(items)//2]
            rucksack2 = items[len(items)//2:]
            common_item = list(set(rucksack1).intersection(rucksack2))[0]
            sum_priorities += abc.index(common_item) + 1 

    return sum_priorities

def part_two():
    sum_priorities = 0

    groups = [lines[k:k+3] for k in range(0, len(lines), 3)]

    for group in groups:
        common_item = list(set(group[0][:-1]).intersection(group[1][:-1]).intersection(group[2][:-1]))[0]
        sum_priorities += abc.index(common_item) + 1 
    return sum_priorities


abc = [x for x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
lines = readfile('inputs/input3.txt')

print(part_one(), part_two()) #7821 2752