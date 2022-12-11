with open("/Users/bryce.cole/advent_of_code_2022/day1/data.txt") as f:
    elfs = []
    cur = 0
    while True:
        line = f.readline()
        if not line:
            elfs.append(cur)
            break
        elif line == "\n":
            elfs.append(cur)
            cur = 0
        else:
            cur += int(line)
elfs.sort()
print(sum(elfs[-3:]))
