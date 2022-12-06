import re 
import copy

def parse_stacks_and_moves():
    stacks = [[] for _ in range(9)]

    with open('inputs/input5.txt') as f:
        lines = f.readlines()
        count = 0

        for line in lines:
            if re.match('\s\d',line):
                break

            crates = re.findall('(\[[A-Z]\]| {3}) ?',line)
            count+=1
            for i,crate in enumerate(crates):
                if (c:=crate.strip(' []')) != '':
                    stacks[i].insert(0,c)
        
        moves = [list((map(int,re.findall('\d+',move)))) for move in [line.strip('\n') for line in lines[count+2:]]]
    return stacks,moves

def part_one(stacks,moves):
    final_stacks = copy.deepcopy(stacks) #stacks will be used for part two
    for move in moves:
        crates,initial_stack,final_stack = move
        for _ in range(crates):
            final_stacks[final_stack-1].append(final_stacks[initial_stack-1].pop())
    
    return ''.join([x[-1] for x in final_stacks])

def part_two(stacks,moves):
    for move in moves:
        crates,initial_stack,final_stack = move

        i_stack = stacks[initial_stack-1]
        stacks[final_stack-1] += i_stack[len(i_stack)-crates:]
        stacks[initial_stack-1] = i_stack[:-crates]

    return ''.join([x[-1] for x in stacks])

#----------------------------------------------------------------
stacks,moves = parse_stacks_and_moves()
print(part_one(stacks,moves),part_two(stacks,moves)) #Right answers: ZBDRNPMVH WDLPFNNNB