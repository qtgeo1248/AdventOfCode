import pprint

pp = pprint.PrettyPrinter()

def main():
    f = open("instructions.txt")
    instr = []
    for line in f:
        instr.append(line.rstrip().split(' '))
    # pp.pprint(instr)
    notFound = True
    visited = [False for _ in range(len(instr))]
    acc = 0
    idx = 0
    while notFound:
        if visited[idx]:
            notFound = False
        else:
            visited[idx] = True
            ins = instr[idx]
            if ins[0] == "nop":
                idx += 1
            elif ins[0] == "acc":
                acc += int(ins[1])
                idx += 1
            elif ins[0] == "jmp":
                idx += int(ins[1])
    print("Answer: " + str(acc))
    f.close()

if __name__ ==  "__main__":
    main()