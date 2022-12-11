def main():
    with open("/Users/bryce.cole/advent_of_code_2022/day6/input.txt") as f:
        data = f.read()
        window = data[:14]
        for i in range(14, len(data)):
            if len(set(window)) == 14:
                print(i)
                break
            window = window[1:] + data[i]


main()
