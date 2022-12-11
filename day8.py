def parse_input():
    trees = []

    with open('inputs/input8.txt') as f:
        for line in f.readlines():
            trees.append([int(tree) for tree in line.strip()])
    return trees

def part_one(trees):
    row_size = len(trees[0])
    visible = (len(trees)*2 - 4) + row_size*2
    
    for i in range(1,len(trees)-1):
        for j in range(1,row_size-1):
            height = trees[i][j]
            top = all([height>h for h in [x[j] for x in trees[:i]]])
            down = all([height>h for h in [x[j] for x in trees[i+1:]]])
            right = all([height>h for h in trees[i][j+1:]])
            left = all([height>h for h in trees[i][:j]])
            if top or down or right or left:
                visible+=1
    return visible

def seen_trees_line(height, row_of_trees):
    seen_trees = 0
    for tree in row_of_trees:
        if height>tree:
            seen_trees += 1
        else:
            if height<=tree:
                seen_trees += 1
            break
    return seen_trees

def part_two(trees):
    highest_score = 0 
    for i in range(1,len(trees)-1):
        for j in range(1,len(trees[0])-1):
            top = seen_trees_line(trees[i][j],[x[j] for x in trees[:i]][::-1])
            down = seen_trees_line(trees[i][j],[x[j] for x in trees[i+1:]])
            right = seen_trees_line(trees[i][j],trees[i][j+1:])
            left = seen_trees_line(trees[i][j],trees[i][:j][::-1])
            
            seen_trees = top*down*right*left
            highest_score = max(seen_trees,highest_score)

    return highest_score

#------------------------------------------------

trees = parse_input()
print(part_one(trees),part_two(trees)) #Right answers: 1849