import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

cycles = 1000000000

def moveNorth(rocks):
    for j in range(len(rocks[0])):
        curCube = 0
        gathered = 0
        for i in range(len(rocks)):
            if rocks[i][j] == 'O':
                rocks[i][j] = '.'
                rocks[curCube + gathered][j] = 'O'
                gathered += 1
            elif rocks[i][j] == '#':
                curCube = i + 1
                gathered = 0

def moveWest(rocks):
    for i in range(len(rocks)):
        curCube = 0
        gathered = 0
        for j in range(len(rocks[0])):
            if rocks[i][j] == 'O':
                rocks[i][j] = '.'
                rocks[i][curCube + gathered] = 'O'
                gathered += 1
            elif rocks[i][j] == '#':
                curCube = j + 1
                gathered = 0

def moveSouth(rocks):
    for j in range(len(rocks[0])):
        curCube = len(rocks) - 1
        gathered = 0
        for i in range(len(rocks)):
            idx = len(rocks) - i - 1
            if rocks[idx][j] == 'O':
                rocks[idx][j] = '.'
                rocks[curCube - gathered][j] = 'O'
                gathered += 1
            elif rocks[idx][j] == '#':
                curCube = idx - 1
                gathered = 0

def moveEast(rocks):
    for i in range(len(rocks)):
        curCube = len(rocks[0]) - 1
        gathered = 0
        for j in range(len(rocks[0])):
            jdx = len(rocks[0]) - j - 1
            if rocks[i][jdx] == 'O':
                rocks[i][jdx] = '.'
                rocks[i][curCube - gathered] = 'O'
                gathered += 1
            elif rocks[i][jdx] == '#':
                curCube = jdx - 1
                gathered = 0

def toTuple(rocks):
    return tuple([tuple(a) for a in rocks])

def weight(rocks):
    tot = 0
    for i in range(len(rocks)):
        for c in rocks[i]:
            if c == 'O':
                tot += len(rocks) - i
    return tot

def main():
    f = open("rocks.txt")

    rocks = []
    for line in f:
        rocks.append([c for c in line.rstrip()])
    tuplefy = toTuple(rocks)
    rockToCycle = {tuplefy : 0}
    cycleToRock = {0 : tuplefy}

    lenCycle = None
    start = None
    for i in range(cycles + 1):
        moveNorth(rocks)
        moveWest(rocks)
        moveSouth(rocks)
        moveEast(rocks)
        tuplefy = toTuple(rocks)
        if tuplefy in rockToCycle:
            lenCycle = i + 1 - rockToCycle[tuplefy]
            start = rockToCycle[tuplefy]
            break
        rockToCycle[tuplefy] = i + 1
        cycleToRock[i + 1] = tuplefy
    pp.pprint(weight(cycleToRock[(cycles - start) % lenCycle + start]))

if __name__ == "__main__":
    main()
