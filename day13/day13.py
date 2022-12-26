def main():
    with open("/Users/bryce.cole/advent_of_code_2022/day13/input.txt") as f:
        results = []
        while True:
            a, b = f.readline().rstrip(), f.readline().rstrip()
            f.readline()
            if a == "" and b == "":
                break
            else:
                a, b = ((eval(a)), (eval(b)))
                results.append(check(a, b))

        ans = sum([i + 1 if v else 0 for i, v in enumerate(results)])
        print(ans)


def check(a, b):
    if type(a) == list:
        a = a[0]
    if type(b) == list:
        b = b[0]

    if x < y:
        return True
    elif x > y:
        return False
    else:
        if len(a) == 0 and len(b) != 0:
            return True
        elif len(a) != 0 and len(b) == 0:
            return False
        else:
            return check(a[1:], b[1:])


def first(x):
    if type(x) == list:
        if not x:
            return 1000
        else:
            return first(x[0])
    else:
        return x


main()
