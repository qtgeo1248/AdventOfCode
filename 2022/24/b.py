import pprint, sys

pp = pprint.PrettyPrinter()

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
nextDirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]

def outBounds(pos, w, h):
    return pos[0] < 0 or pos[0] >= w or pos[1] < 0 or pos[1] >= h

def canMakeIt(pos, curTrip, maxT, curT, w, h, blizzards, brain):
    if maxT <= 0:
        return curT if (pos == (w - 1, h) and curTrip % 2 == 0) or (pos == (0, -1) and curTrip == 1) else None
    if pos == (w - 1, h) and curTrip % 2 == 0:
        return curT
    if pos == (0, -1) and curTrip == 1:
        return curT
    if outBounds(pos, w, h) and pos != (0, -1) and pos != (w - 1, h):
        return None
    if pos != (0, -1) and pos != (w - 1, h):
        for dirI, dir in enumerate(dirs):
            potential = ((pos[0] - dir[0] * curT) % w, (pos[1] - dir[1] * curT) % h)
            if (potential, dirI) in blizzards:
                return None
    if (pos, curTrip, maxT, curT) in brain:
        return brain[(pos, curTrip, maxT, curT)]
    curMin = None
    for dir in nextDirs:
        nextPos = (pos[0] + dir[0], pos[1] + dir[1])
        nextTime = canMakeIt(nextPos, curTrip, maxT - 1, curT + 1, w, h, blizzards, brain)
        if nextTime is not None:
            curMin = nextTime if curMin is None or nextTime < curMin else curMin
    brain[(pos, curTrip, maxT, curT)] = curMin
    return curMin

def main():
    f = open("map.txt")

    blizzards = set()
    w, h = 0, -1

    for line in f:
        line = line.strip()[1:-1]
        w = len(line)
        for j, cell in enumerate(line):
            if cell == ">":
                blizzards.add(((j, h), 0))
            elif cell == "v":
                blizzards.add(((j, h), 1))
            elif cell == "<":
                blizzards.add(((j, h), 2))
            elif cell == "^":
                blizzards.add(((j, h), 3))
        h += 1
    h -= 1
    brain = dict()
    t = 0
    trips = [None, None, None]
    while trips[0] is None:
        t += 100
        trips[0] = canMakeIt((0, -1), 0, t, 0, w, h, blizzards, brain)
    while trips[1] is None:
        t += 100
        trips[1] = canMakeIt((w - 1, h), 1, t, trips[0], w, h, blizzards, brain)
    while trips[2] is None:
        t += 100
        trips[2] = canMakeIt((0, -1), 2, t, trips[1], w, h, blizzards, brain)
    print(trips[2])

if __name__ == "__main__":
    main()
