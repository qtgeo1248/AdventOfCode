import pprint

pp = pprint.PrettyPrinter()

dirs = [
    (-1, 0),    # N
    (1, 0),     # S
    (0, -1),    # W
    (0, 1)      # E
]

def addLoc(newLocs, loc):
    if loc not in newLocs:
        newLocs[loc] = 1
    else:
        newLocs[loc] += 1

def noNeighs(elves, elf):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy != 0 or dx != 0:
                if (elf[0] + dy, elf[1] + dx) in elves:
                    return False
    return True

def doRound(elves, offset):
    proposals = dict()
    newLocs = dict()
    for elf in elves:
        if noNeighs(elves, elf):
            proposals[elf] = (0, 0)
            addLoc(newLocs, elf)
        else:
            for i in range(4):
                dir = dirs[(i + offset) % 4]
                isValid = True
                if dir[0] == 0:
                    for dy in range(-1, 2):
                        if (elf[0] + dy, elf[1] + dir[1]) in elves:
                            isValid = False
                else:
                    for dx in range(-1, 2):
                        if (elf[0] + dir[0], elf[1] + dx) in elves:
                            isValid = False
                if isValid and elf not in proposals:
                    proposals[elf] = dir
                    newLoc = (elf[0] + dir[0], elf[1] + dir[1])
                    addLoc(newLocs, newLoc)
            if elf not in proposals:
                proposals[elf] = (0, 0)
                addLoc(newLocs, elf)
    newElves = set()
    notDone = False
    for elf in elves:
        dir = proposals[elf]
        newLoc = (elf[0] + dir[0], elf[1] + dir[1])
        if newLocs[newLoc] == 1:
            newElves.add(newLoc)
            if newLoc != elf:
                notDone = True
        else:
            newElves.add(elf)
    return newElves, notDone

def main():
    f = open("grove.txt")

    elves = set()
    row = 0
    for line in f:
        for j in range(len(line)):
            if line[j] == "#":
                elves.add((row, j))
        row += 1
    i = 0
    notDone = True
    while notDone:
        elves, notDone = doRound(elves, i)
        i += 1
    print(i)

if __name__ == "__main__":
    main()
