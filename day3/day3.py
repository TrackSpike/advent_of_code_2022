def main():
    total = 0
    with open("/Users/bryce.cole/advent_of_code_2022/day3/input.txt") as f:
        while True:
            line1, line2, line3 = (
                f.readline().rstrip(),
                f.readline().rstrip(),
                f.readline().rstrip(),
            )
            if not line1:
                break
            total += calculate(find_shared(line1, line2, line3))
    print(total)


def find_shared(line1, line2, line3):
    line1, line2, line3 = set(line1), set(line2), set(line3)
    return list(line1 & line2 & line3)[0]


def calculate(c):
    if c.isupper():
        return ord(c) - 64 + 26
    else:
        return ord(c) - 96


main()
