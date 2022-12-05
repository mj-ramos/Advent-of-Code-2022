def part_one():
    max_calories = 0
    elf_calories = 0

    for line in lines:
        if line=='\n':
            if elf_calories>max_calories:
                max_calories = elf_calories
            elf_calories = 0
        else:
            elf_calories += int(line.strip())
            
    return max_calories

def part_two():
    top_calories = [0,0,0]
    elf_calories = 0

    for line in lines:
        if line=='\n':
            min_calories = min(top_calories)
            if elf_calories > min_calories:
                top_calories[top_calories.index(min_calories)] = elf_calories
            elf_calories=0
        else:
            elf_calories += int(line.strip())
            
    return sum(top_calories)

#------------------------------------------------------------------------------------

with open('inputs/input1.txt') as f:
    lines = f.readlines()

print(part_one(),part_two()) #Right answers: 69206 197400