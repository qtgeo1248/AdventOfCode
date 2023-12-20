import math
import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def lenPath(cur, nodes, instrs):
    steps = 0
    while cur[-1] != 'Z':
        instr = instrs[steps % len(instrs)]
        cur = nodes[cur][0 if instr == 'L' else 1]
        steps += 1
    return steps

def main():
    f = open("map.txt")

    instrs = f.readline().rstrip()
    nodes = dict()
    f.readline()
    allAs = set()
    for line in f:
        parts = line.rstrip().split(" = ")
        nexts = parts[1].split(", ")
        nodes[parts[0]] = (nexts[0][1:], nexts[1][:-1])
        if parts[0][-1] == 'A':
            allAs.add(parts[0])
    steps = [lenPath(cur, nodes, instrs) for cur in allAs]
    lcm = 1
    for step in steps:
        lcm = math.lcm(lcm, step) 
    print(lcm)

if __name__ == "__main__":
    main()
