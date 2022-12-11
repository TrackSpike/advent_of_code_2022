def calculate_score(data, loc):
    width, height = len(data[0]), len(data)
    sx, sy = loc
    v = data[sx][sy]
    left, right, up, down = 0, 0, 0, 0
    for x in range(sx + 1, width):
        right += 1
        if data[x][sy] >= v:
            break

    for y in range(sy + 1, height):
        down += 1
        if data[sx][y] >= v:
            break

    for x in range(sx - 1, -1, -1):
        left += 1
        if data[x][sy] >= v:
            break

    for y in range(sy - 1, -1, -1):
        up += 1
        if data[sx][y] >= v:
            break

    result = left * right * up * down
    if result == 252000:
        print(loc)
    return result


def main():
    with open("/Users/bryce.cole/advent_of_code_2022/day8/input.txt") as f:
        data = f.readlines()
        data = [[int(i) for i in e.rstrip()] for e in data]
        width, height = len(data[0]), len(data)
        seen = set()

        for x in range(width):
            mini = -1
            for y in range(height):
                if data[x][y] > mini:
                    seen.add((x, y))
                    mini = data[x][y]

        for x in range(width):
            mini = -1
            for y in range(height - 1, -1, -1):
                if data[x][y] > mini:
                    seen.add((x, y))
                    mini = data[x][y]

        for y in range(height):
            mini = -1
            for x in range(width):
                if data[x][y] > mini:
                    seen.add((x, y))
                    mini = data[x][y]

        for y in range(height):
            mini = -1
            for x in range(width - 1, -1, -1):
                if data[x][y] > mini:
                    seen.add((x, y))
                    mini = data[x][y]

        print(len(seen))

        result = ""
        for y in range(height):
            for x in range(width):
                result += str(data[x][y]) if (x, y) in seen else " "
            result += "\n"
        print(result)

        # print(max([calculate_score(data, e) for e in seen]))


main()
