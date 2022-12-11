import pprint

pp = pprint.PrettyPrinter()

def op(worry, type):
    if type == "S":
        return worry * worry
    (t, n) = type
    if t == "M":
        return worry * n
    else:
        return worry + n

def main():
    f = open("monkeys.txt")

    monkeyItems = []
    monkeyOps = []
    monkeyTests = []
    monkeyTrues = []
    monkeyFalses = []
    monkeySeen = []
    numMonkeys = 0

    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        elif line[0] == "M":
            monkeySeen.append(0)
            numMonkeys += 1
        elif line[0] == "S":
            [_, items] = line.split(": ")
            items = items.split(", ")
            monkeyItems.append([int(x) for x in items])
        elif line[0] == "O":
            [_, items] = line.split(" = ")
            checkAdd = items.split(" + ")
            checkMul = items.split(" * ")
            if len(checkAdd) > 1:
                monkeyOps.append(("A", int(checkAdd[1])))
            elif checkMul[1] == "old":
                monkeyOps.append("S")
            else:
                monkeyOps.append(("M", int(checkMul[1])))
        elif line[0] == "T":
            line = line.split()
            monkeyTests.append(int(line[-1]))
        elif line[3] == "t":
            line = line.split()
            monkeyTrues.append(int(line[-1]))
        elif line[3] == "f":
            line = line.split()
            monkeyFalses.append(int(line[-1]))

    for _ in range(20):
        for i in range(numMonkeys):
            monkeySeen[i] += len(monkeyItems[i])
            for item in monkeyItems[i]:
                nextIt = op(item, monkeyOps[i])
                nextIt //= 3
                if nextIt % monkeyTests[i] == 0:
                    monkeyItems[monkeyTrues[i]].append(nextIt)
                else:
                    monkeyItems[monkeyFalses[i]].append(nextIt)
            monkeyItems[i] = []

    monkeySeen.sort()
    print(monkeySeen[-1] * monkeySeen[-2])
if __name__ == "__main__":
    main()