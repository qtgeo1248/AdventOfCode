import pprint

pp = pprint.PrettyPrinter()

def main():
    f = open("procedure.txt")
    stacks = []
    tot = 0
    for line in f:
        if line[0] == "m":
            line = line.strip().split()
            numMove = int(line[1])
            fro = int(line[3])
            to = int(line[5])
            for _ in range(numMove):
                stacks[to - 1].append(stacks[fro - 1].pop())

        elif line[0] == "\n":
            for i in range(tot):
                stacks[i].pop()
                stacks[i].reverse()
        else:
            if len(stacks) == 0:
                tot = len(line) // 4
                stacks = [[] for _ in range(tot)]
            for i in range(tot):
                c = line[4 * i + 1]
                if c != " ":
                    stacks[i].append(c)
    ans = ""
    for stack in stacks:
        ans += stack[-1]
    print(ans)

if __name__ == "__main__":
    main()