import pprint

pp = pprint.PrettyPrinter()

def want(cycle):
    return (cycle - 20) % 40 == 0

def main():
    f = open("program.txt")

    cycle = 1
    x = 1
    total = 0

    for line in f:
        line = line.strip().split()
        if cycle > 220:
            break
        if want(cycle):
            total += x * cycle
        cycle += 1
        if line[0] == "addx":
            if cycle > 220:
                break
            if want(cycle):
                total += x * cycle
            x += int(line[1])
            cycle += 1
    print(total)


if __name__ == "__main__":
    main()