
def main():
    with open(r"/day10/input.txt") as f:
        cycle, x = 0, 1
        process = (False, 0)

        while True:
            cycle += 1
            print("#" if abs((cycle % 40) - 1 - x) <= 1 else ".", end="")
            if cycle % 40 == 0:
                print()

            if not process[0]:
                line = f.readline().rstrip()
                if not line:
                    break

                opcode = line[:4]
                if opcode == "addx":
                    arg1 = int(line[5:])
                    process = (True, arg1)
                elif opcode == "noop":
                    pass
                else:
                    raise Exception("Invalid Opcode")
            else:
                x += process[1]
                process = (False, 0)


main()
