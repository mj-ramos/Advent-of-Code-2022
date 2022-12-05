def parse_pairs():
    pairs = []

    with open('inputs/input4.txt') as f:
        lines = f.readlines()

    for line in lines:
        sections = line.strip('\n').split(',')
        elf1 = tuple(map(int,sections[0].split('-')))
        elf2 = tuple(map(int,sections[1].split('-')))
        pairs.append((elf1,elf2))

    return pairs


def part_one(pairs):
    contained = 0

    for pair in pairs:
        elf1_min, elf1_max = pair[0]
        elf2_min, elf2_max = pair[1]

        if (elf1_min >= elf2_min and elf1_max <= elf2_max) or (elf2_min >= elf1_min and elf2_max <= elf1_max):
            contained += 1

    return contained

def part_two(pairs):
    overlapped = 0

    for pair in pairs:
        elf1_min, elf1_max = pair[0]
        elf2_min, elf2_max = pair[1]
    
        if (elf1_min >= elf2_min or elf1_max >= elf2_min) and (elf2_min >= elf1_min or elf2_max >= elf1_min):
            overlapped += 1

    return overlapped

#------------------------------------------------------------------------------------

pairs = parse_pairs()
print(part_one(pairs),part_two(pairs)) #Right answers: 580 895