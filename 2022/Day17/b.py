import pprint

pp = pprint.PrettyPrinter()

alltypes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (1, 0), (0, 1), (1, 1)]
]

topMosts = [0, 2, 2, 3, 1]
totNeed = 1000000000000

def addRock(rocks, coord):
    if coord[0] >= len(rocks):
        for _ in range(coord[0] - len(rocks) + 1):
            rocks.append([False for _ in range(7)])
    rocks[coord[0]][coord[1]] = True

def hasRock(rocks, coord):
    if coord[0] >= len(rocks):
        for _ in range(coord[0] - len(rocks) + 1):
            rocks.append([False for _ in range(7)])
    return rocks[coord[0]][coord[1]]

def move(curRock, rocks, h, jets, i):
    start = (h, 2)
    def isDone():
        for dir in curRock:
            if hasRock(rocks, (start[0] + dir[0] - 1, start[1] + dir[1])):
                for dirr in curRock:
                    addRock(rocks, (start[0] + dirr[0], start[1] + dirr[1]))
                return True
        return False
    def canMove(d):
        for dir in curRock:
            pt = (start[0] + dir[0], start[1] + dir[1])
            if pt[1] + d < 0 or pt[1] + d > 6 or hasRock(rocks, (pt[0], pt[1] + d)):
                return False
        return True

    notDone = True
    while notDone:
        if jets[i] == "<" and canMove(-1):
            start = (start[0], start[1] - 1)
        if jets[i] == ">" and canMove(1):
            start = (start[0], start[1] + 1)
        if isDone():
            notDone = False
        else:
            start = (start[0] - 1, start[1])
        i = (i + 1) % len(jets)
    return (start[0], i)

def getKey(rocks, height):
    key = [tuple(row) for row in rocks[-150:(height + 1)]]
    return tuple(key)

def main():
    f = open("jets.txt")

    stream = f.readline().strip()
    rocks = [[True for _ in range(7)]]
    height = 0
    jetI = 0
    brain = dict()

    cycle = None
    i = 0
    while i < totNeed:
        (nexH, jetI) = move(alltypes[i % 5], rocks, height + 4, stream, jetI)
        height = max(height, nexH + topMosts[i % 5])
        info = (getKey(rocks, height), i % 5, jetI)
        if info in brain:
            cycle = (height - brain[info][0], i - brain[info][1])
            break
        else:
            brain[info] = (height, i)
        i += 1
    toMult = (totNeed - i - 1) // cycle[1]
    toLeft = (totNeed - i - 1) % cycle[1]
    prevHeight = height
    actHeight = height + cycle[0] * toMult

    for j in range(toLeft):
        (nexH, jetI) = move(alltypes[(i + j + 1) % 5], rocks, height + 4, stream, jetI)
        height = max(height, nexH + topMosts[(i + j + 1) % 5])
    print(actHeight + height - prevHeight)

if __name__ == "__main__":
    main()
