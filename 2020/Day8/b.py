import pprint

pp = pprint.PrettyPrinter()

def tryChange(instr):
    visited = [False for _ in range(len(instr))]
    acc = 0
    i = 0
    while i < len(instr):
        if visited[i]:
            return None
        visited[i] = True
        if instr[i][0] == "nop":
            i += 1
        elif instr[i][0] == "acc":
            acc += int(instr[i][1])
            i += 1
        elif instr[i][0] == "jmp":
            i += int(instr[i][1])
    return acc

def main():
    f = open("instructions.txt")
    instr = []
    for line in f:
        instr.append(line.rstrip().split(' '))
    # pp.pprint(instr)

    ans = None
    i = 0
    while ans is None:
        if instr[i][0] == "jmp":
            instr[i][0] = "nop"
            attempt = tryChange(instr)
            if attempt is not None:
                ans = attempt
            instr[i][0] = "jmp"
        elif instr[i][0] == "nop":
            instr[i][0] = "jmp"
            attempt = tryChange(instr)
            if attempt is not None:
                ans = attempt
            instr[i][0] = "nop"
        i += 1

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()