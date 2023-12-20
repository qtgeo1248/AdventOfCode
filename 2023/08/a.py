import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def main():
    f = open("map.txt")

    instrs = f.readline().rstrip()
    nodes = dict()
    f.readline()
    for line in f:
        parts = line.rstrip().split(" = ")
        nexts = parts[1].split(", ")
        nodes[parts[0]] = (nexts[0][1:], nexts[1][:-1])
    cur = 'AAA'
    steps = 0
    while cur != 'ZZZ':
        instr = instrs[steps % len(instrs)]
        if instr == 'L':
            cur = nodes[cur][0]
        else:
            cur = nodes[cur][1]
        steps += 1
    print(steps)


if __name__ == "__main__":
    main()
