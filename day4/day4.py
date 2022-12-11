def main():
    total = 0
    with open("/Users/bryce.cole/advent_of_code_2022/day4/input.txt") as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break
            a, b = line.split(",")
            a, b = a.split("-"), b.split("-")
            a, b = tuple(map(int, a)), tuple(map(int, b))
            if check(a, b):
                print(a, b)
                total += 1

    print(total)


def check(a, b):
    return a[0] <= b[1] and a[1] >= b[0]


main()
