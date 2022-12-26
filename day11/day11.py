import math


class Monkey:
    def __init__(self, name, starting_items, operation, test) -> None:
        self.name = name
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.inspected_item_count = 0
        self.magic_number = None

    def inspect(self, monkeys):
        while self.starting_items:
            self.inspected_item_count += 1
            item = self.starting_items.pop(0)
            item = eval(self.operation)
            item = item % self.magic_number
            if item % self.test[0] == 0:
                monkeys[self.test[1]].starting_items.append(item)
            else:
                monkeys[self.test[2]].starting_items.append(item)

    def __str__(self) -> str:
        return f"Monkey {self.name} has {self.starting_items}."

    def __repr__(self) -> str:
        return f"Monkey {self.name} has {self.starting_items}."


def main():
    with open("/Users/bryce.cole/advent_of_code_2022/day11/input.txt") as f:
        prev, line = None, None
        name, starting_items, operation, test = "", [], "", ["", "", ""]
        monkeys = []
        while True:
            prev = line
            line = f.readline().rstrip()
            if not line and not prev:
                break
            elif line.startswith("Monkey"):
                name = int(line.split(" ")[-1][:-1])
            elif line.startswith("  Starting"):
                starting_items = [int(i) for i in line[18:].split(", ")]
            elif line.startswith("  Operation"):
                operation = line[19:].replace("old", "item")
            elif line.startswith("  Test"):
                test[0] = int(line.split(" ")[-1])
            elif line.startswith("    If true"):
                test[1] = int(line.split(" ")[-1])
            elif line.startswith("    If false"):
                test[2] = int(line.split(" ")[-1])
            elif not line:
                monkeys.append(Monkey(name, starting_items, operation, test.copy()))

    # Magic Number
    magic_number = math.prod([m.test[0] for m in monkeys])
    for m in monkeys:
        m.magic_number = magic_number

    # Monkey Business
    rounds = 10000
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.inspect(monkeys)

    monkeys.sort(key=lambda m: m.inspected_item_count, reverse=True)
    print(monkeys[0].inspected_item_count * monkeys[1].inspected_item_count)


main()
