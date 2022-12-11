def main():
    stacks = [
        ["Q", "M", "G", "C", "L"],
        ["R", "D", "L", "C", "T", "F", "H", "G"],
        ["V", "J", "F", "N", "M", "T", "W", "R"],
        ["J", "F", "D", "V", "Q", "P"],
        ["N", "F", "M", "S", "L", "B", "T"],
        ["R", "N", "V", "H", "C", "D", "P"],
        ["H", "C", "T"],
        ["G", "S", "J", "V", "Z", "N", "H", "P"],
        ["Z", "F", "H", "G"],
    ]

    with open("/Users/bryce.cole/advent_of_code_2022/day5/input.txt") as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            amount, start, end = [int(i) for i in line.split() if i.isdigit()]
            stacks[end - 1].extend(stacks[start - 1][-amount:])
            del stacks[start - 1][-amount:]

        print("".join([s[-1] for s in stacks]))


main()
