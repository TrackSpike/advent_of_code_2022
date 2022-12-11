def calculate(a, b):
    score = 0
    if b == "X":
        score += 1
    elif b == "Y":
        score += 2
    elif b == "Z":
        score += 3

    if a == "A":
        if b == "X":
            score += 3
        elif b == "Y":
            score += 6
        elif b == "Z":
            score += 0
    elif a == "B":
        if b == "X":
            score += 0
        elif b == "Y":
            score += 3
        elif b == "Z":
            score += 6
    elif a == "C":
        if b == "X":
            score += 6
        elif b == "Y":
            score += 0
        elif b == "Z":
            score += 3

    return score


def find_value(a, x):
    if a == "A":
        if x == "X":
            return "Z"
        elif x == "Y":
            return "X"
        elif x == "Z":
            return "Y"
    elif a == "B":
        if x == "X":
            return "X"
        elif x == "Y":
            return "Y"
        elif x == "Z":
            return "Z"
    elif a == "C":
        if x == "X":
            return "Y"
        elif x == "Y":
            return "Z"
        elif x == "Z":
            return "X"


with open("/Users/bryce.cole/advent_of_code_2022/day2/input.txt") as f:
    score = 0
    while True:
        line = f.readline()
        if not line:
            break
        a, b = line[0], line[2]
        b = find_value(a, b)
        score += calculate(a, b)

print(score)
