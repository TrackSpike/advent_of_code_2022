import re
from collections import defaultdict


class Scanner:
    def __init__(self, sensors, beacons, mapping) -> None:
        self.sensors = sensors
        self.beacons = beacons
        self.mapping = mapping
        self.calculated = set()
        self.magic_number = 2000000

    def debug(self):
        all = self.sensors.union(self.beacons)
        xMax = max([e[0] for e in all]) + 10
        xMin = min([e[0] for e in all]) - 10
        yMax = max([e[1] for e in all]) + 10
        yMin = min([e[1] for e in all]) - 10
        for y in range(yMin, yMax):
            for x in range(xMin, xMax):
                c = "."
                if y == self.magic_number and x in self.calculated:
                    c = "#"
                if (x, y) in self.sensors:
                    c = "S"
                if (x, y) in self.beacons:
                    c = "B"
                print(c, end="")
            print("")

    def mark_fast(self, sensor, beacon):
        sx, sy = sensor
        d = dist(sensor, beacon)
        for y in range(-d, d + 1):
            for x in range(-(d - abs(y)), d - abs(y) + 1):
                if y + sy == self.magic_number:
                    self.calculated.add(x + sx)

    def mark_hyper(self, sensor, beacon):
        sx, sy = sensor
        d = dist(sensor, beacon)
        j = abs(self.magic_number - sy)
        if j > d:
            return

        for x in range(-(d - j), d - j + 1):
            if (x + sx, self.magic_number) not in self.beacons:
                self.calculated.add(x + sx)

    def count_row(self):
        return len(self.calculated)


def dist(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def main():
    sensors, beacons = set(), set()
    mapping = {}
    with open("/Users/bryce.cole/advent_of_code_2022/day15/input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            m = re.findall(r"-*[0-9]+", line)
            sensor = (int(m[0]), int(m[1]))
            beacon = (int(m[2]), int(m[3]))
            sensors.add(sensor)
            beacons.add(beacon)
            mapping[sensor] = beacon
    scan = Scanner(sensors, beacons, mapping)
    print("built")
    for s, b in mapping.items():
        scan.mark_hyper(s, b)
        print(f"Marked {s}")
    print(scan.count_row())


main()
