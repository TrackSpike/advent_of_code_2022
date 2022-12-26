from collections import defaultdict


def main():
    spawner = (500, 0)
    particles = defaultdict(lambda: "")
    for l in open("/Users/bryce.cole/advent_of_code_2022/day14/input.txt"):
        p = [*map(lambda x: tuple(map(int, (x.split(",")))), l.split(" -> "))]

        for i in range(1, len(p)):
            p1, p2 = p[i - 1], p[i]

            if p1[0] == p2[0]:
                for y in range(min([p1[1], p2[1]]), max([p1[1], p2[1]]) + 1):
                    particles[(p1[0], y)] = "#"
            elif p1[1] == p2[1]:
                for x in range(min([p1[0], p2[0]]), max([p1[0], p2[0]]) + 1):
                    particles[(x, p1[1])] = "#"
            else:
                assert False
    cave = Cave(particles)
    sand = 0
    while cave.sim(spawner):
        sand += 1
    print(sand)
    cave.debug()


def down(start):
    return (start[0], start[1] + 1)


def down_left(start):
    return (start[0] - 1, start[1] + 1)


def down_right(start):
    return (start[0] + 1, start[1] + 1)


class Cave:
    def __init__(self, state) -> None:
        self.state = state

    def sim(self, start):
        while True:
            if start[1] > 400:
                return False
            if self.state[down(start)] == "":
                start = down(start)
            elif self.state[down_left(start)] == "":
                start = down_left(start)
            elif self.state[down_right(start)] == "":
                start = down_right(start)
            else:
                self.state[start] = "o"
                return True

    def debug(self):
        for y in range(0, 250):
            for x in range(470, 570):
                c = "."
                if self.state[(x, y)] == "#":
                    c = "#"
                if self.state[(x, y)] == "o":
                    c = "o"
                if (x, y) == (500, 0):
                    c = "+"
                print(c, end="")
            print("")
        print("")


main()
