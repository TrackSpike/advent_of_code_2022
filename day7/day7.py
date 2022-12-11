big_dirs = []


class Dir:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.files = []
        self.parent = parent

    def __str__(self) -> str:
        return f"{self.name} : {self.files}"

    def __repr__(self) -> str:
        return f"{self.name} : {self.files}"

    def get_size(self) -> int:
        sizes = []
        for e in self.files:
            if isinstance(e, Dir):
                sizes.append(e.get_size())
            else:
                sizes.append(e.size)
        size = sum(sizes)
        big_dirs.append(size)
        return size


class File:
    def __init__(self, name, size, parent) -> None:
        self.name = name
        self.size = size
        self.parent = parent

    def __str__(self) -> str:
        return f"{self.name} : {self.size}"

    def __repr__(self) -> str:
        return f"{self.name} : {self.size}"


def main():
    with open("/Users/bryce.cole/advent_of_code_2022/day7/input.txt") as f:
        line = f.readline().rstrip()
        root = Dir("/", None)
        cur = root
        while True:
            line = f.readline().rstrip()
            if not line:
                break

            if line.startswith("$ ls"):
                while True:
                    pos = f.tell()
                    line = f.readline().rstrip()
                    if line.startswith("$"):
                        f.seek(pos)
                        break
                    elif len(line) > 0:
                        arg1, arg2 = line.split(" ")
                        if line.startswith("dir"):
                            cur.files.append(Dir(arg2, cur))
                        else:
                            cur.files.append(File(arg2, int(arg1), cur))
                    else:
                        break

            elif line.startswith("$ cd"):
                print(line)
                dir_name = line.split(" ")[2]
                if dir_name == "..":
                    cur = cur.parent
                elif dir_name == "/":
                    cur = root
                else:
                    cur = next((item for item in cur.files if item.name == dir_name))

    free = 70000000 - root.get_size()
    update = 30000000
    needed = update - free
    ans = float("inf")
    for s in big_dirs:
        if s >= needed and s < ans:
            ans = s

    print(ans)


main()
