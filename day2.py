def part_one():
    #Points: 
    #   - 0 if you lost, 3 if the round was a draw, and 6 if you won
    #   - 1 for Rock, 2 for Paper, and 3 for Scissors

    #A for Rock, B for Paper, and C for Scissors.
    #X for Rock, Y for Paper, and Z for Scissors.

    draw = {'A':'X', 'B':'Y', 'C':'Z'}
    win = {'A':'Y', 'B':'Z', 'C':'X'} #paper(Y) wins rock(A) etc.
    points = {'X':1,'Y':2,'Z':3}

    score = 0

    for line in lines:
        round = line.split()
        score+=points[round[1]]

        if (draw[round[0]]==round[1]):
            score+=3
        elif win[round[0]]==round[1]:
            score+=6

    return score
    
def part_two():
    #X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

    win = {'A':'B', 'B':'C', 'C':'A'}  #to win rock(A), play paper(B) etc.
    points = {'A':1,'B':2,'C':3}

    score = 0

    for line in lines:
        round = line.split()
        if (round[1] == 'X'):
            score += sum(points.values()) - points[win[round[0]]] - points[round[0]] 
        elif (round[1] == 'Y'):
            score += 3 + points[round[0]]
        elif (round[1] == 'Z'):
            score += 6 + points[win[round[0]]]

    return score

#------------------------------------------------------------------------------------

with open('inputs/input2.txt') as f:
    lines = f.readlines()

print(part_one(),part_two()) #Right answers: 13809 12316