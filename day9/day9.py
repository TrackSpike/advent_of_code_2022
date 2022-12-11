import os
import time


def print_out(nodes):
    width, height = 150, 200
    for y in range(height - 1, -50, -1):
        for x in range(-70, width):
            c = " "
            for i in range(len(nodes) - 1, -1, -1):
                if nodes[i].x == x and nodes[i].y == y:
                    c = str(i)
                    if i == len(nodes) - 1:
                        c = "T"
                    if i == 0:
                        c = "H"
            print(c, end="")
        print()
    print()


def main():
    with open("/Users/bryce.cole/advent_of_code_2022/day9/input.txt") as f:
        length = 10
        nodes = [Cord(0, 0) for _ in range(10)]
        while True:
            line = f.readline().rstrip()
            if not line:
                break

            direction, amount = line.split(" ")
            amount = int(amount)
            # print(direction, amount)
            for _ in range(amount):
                nodes[0].move(direction)
                for i in range(1, len(nodes)):
                    if nodes[i].dist(nodes[i - 1]) > 1:
                        nodes[i].moveTowards(nodes[i - 1])
                os.system("clear")
                print_out(nodes)
                time.sleep(0.1)

        print(len(nodes[-1].traveled))
        xs = [e[0] for e in nodes[0].traveled]
        ys = [e[1] for e in nodes[0].traveled]

        print(f"{min(xs)} {min(ys)}")
        print(f"{max(xs)} {max(ys)}")


class Cord:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.traveled = set()
        self.traveled.add((0, 0))

    def dist(self, other):
        return max(abs(self.x - other.x), abs(self.y - other.y))

    def move(self, direction):
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "L":
            self.x -= 1
        elif direction == "R":
            self.x += 1
        elif direction == "UR":
            self.x += 1
            self.y += 1
        elif direction == "DR":
            self.x += 1
            self.y -= 1
        elif direction == "DL":
            self.x -= 1
            self.y -= 1
        elif direction == "UL":
            self.x -= 1
            self.y += 1
        else:
            raise Exception("Bad input")
        self.traveled.add((self.x, self.y))

    def moveTowards(self, other):
        xDiff, yDiff = other.x - self.x, other.y - self.y
        if xDiff == 0 and yDiff == 0:
            return

        elif xDiff == 0:
            if yDiff > 0:
                self.move("U")
            else:
                self.move("D")

        elif yDiff == 0:
            if xDiff > 0:
                self.move("R")
            else:
                self.move("L")

        elif xDiff > 0 and yDiff > 0:
            self.move("UR")
        elif xDiff > 0 and yDiff < 0:
            self.move("DR")

        elif xDiff < 0 and yDiff > 0:
            self.move("UL")
        elif xDiff < 0 and yDiff < 0:
            self.move("DL")


main()
