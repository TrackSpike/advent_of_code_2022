from collections import defaultdict

# dropped example from 741 to 41 wow


class Solver:
    def __init__(self) -> None:
        self.finish_spot = None, None
        self.data = self.parse_data()
        self.starting_points = self.get_starting_points()
        self.scores = defaultdict(lambda: float("inf"))
        self.moves = 0

    def get_available_tiles(self, x, y, path):
        h, w = len(self.data), len(self.data[0])
        score = len(path)
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
                and self.data[new_cord[1]][new_cord[0]] - height <= 1
                and score < self.scores[new_cord]
            ):
                result.append(new_cord)
                self.scores[new_cord] = score
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
            c = "a"
        return ord(c) - 96

    def bfs(self, starting_point):
        queue = [[starting_point]]
        while queue:
            cur = queue.pop(0)
            node = cur[-1]
            self.moves += 1
            if node == self.finish_spot:
                print(f"Found at {len(cur)-1} with {self.moves}")
                self.debug_path(cur)
                return len(cur) - 1
            else:
                options = [cur + [a] for a in self.get_available_tiles(*node, cur)]
                queue.extend(options)
        return float("inf")

    def get_starting_points(self):
        h, w = len(self.data), len(self.data[0])
        result = []
        for x in range(w):
            for y in range(h):
                if self.data[y][x] == 1:
                    result.append((x, y))
        return result

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
    r = min([s.bfs(p) for p in s.starting_points])
    print(r)


main()
