from collections import defaultdict

# dropped example from 741 to 41 wow


class Solver:
    def __init__(self) -> None:
        self.starting_location, self.finish_spot = None, None
        self.data = self.parse_data()
        h, w = len(self.data), len(self.data[0])
        for y in range(h):
            for x in range(w):
                self.graph[(x, y)] = self.get_available_tiles()

        self.scores = defaultdict(lambda: float("inf"))
        self.scores[self.starting_location] = 0
        self.moves = 0

    def get_available_tiles(self, x, y):
        h, w = len(self.data), len(self.data[0])
        height = self.data[y][x]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        for d in dirs:
            new_cord = (x + d[0], y + d[1])
            if (
                new_cord[0] >= 0
                and new_cord[1] >= 0
                and new_cord[0] < w
                and new_cord[1] < h
                and abs(height - self.data[new_cord[1]][new_cord[0]]) <= 1
            ):
                result.append(new_cord)
        return result

    def parse_data(self):
        with open("/Users/bryce.cole/advent_of_code_2022/day12/input.txt") as f:
            return [
                [self.convert(b, x, y) for x, b in enumerate(a.rstrip())]
                for y, a in enumerate(f.readlines())
            ]

    def convert(self, c, x, y):
        if c == "E":
            self.finish_spot = (x, y)
            c = "z"
        if c == "S":
            self.starting_location = (x, y)
            c = "a"
        return ord(c) - 96

    def bfs(self):
        queue = [[self.starting_location]]
        while queue:
            cur = queue.pop(0)
            node = cur[-1]
            self.moves += 1
            if node == self.finish_spot:
                print(f"Found {cur} at {len(cur)-1} with {self.moves}")
                break
            else:
                options = [cur + [a] for a in self.get_available_tiles(*node, cur)]
                queue.extend(options)

    def debug_path(self, path):
        h, w = len(self.data), len(self.data[0])
        for y in range(h):
            for x in range(w):
                if (x, y) in path:
                    i = path.index((x, y))
                    if i == len(path) - 1:
                        print("X", end="")
                    else:
                        n = path[i + 1]
                        diff = (n[0] - x, n[1] - y)
                        if diff == (1, 0):
                            print(">", end="")
                        elif diff == (0, 1):
                            print("V", end="")
                        elif diff == (-1, 0):
                            print("<", end="")
                        elif diff == (0, -1):
                            print("^", end="")
                else:
                    print(".", end="")
            print()
        print()


def main():
    s = Solver()
    s.bfs()


main()
