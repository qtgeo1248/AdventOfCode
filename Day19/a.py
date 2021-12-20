import pprint
import math

numRots = 24
pp = pprint.PrettyPrinter()

def rotate(p, rot):
    # Facing +z dir
    if rot == 0: # (+x, +y, +z)
        return p
    elif rot == 1: # (-y, +x, +z)
        return (-p[1], p[0], p[2])
    elif rot == 2: # (-x, -y, +z)
        return (-p[0], -p[1], p[2])
    elif rot == 3: # (+y, -x, +z)
        return (p[1], -p[0], p[2])
    # Facing -z dir
    elif rot == 4: # (+y, +x, -z)
        return (p[1], p[0], -p[2])
    elif rot == 5: # (-x, +y, -z)
        return (-p[0], p[1], -p[2])
    elif rot == 6: # (-y, -x, -z)
        return (-p[1], -p[0], -p[2])
    elif rot == 7: # (+x, -y, -z)
        return (p[0], -p[1], -p[2])
    # Facing +x dir
    elif rot == 8: # (+y, +z, +x)
        return (p[1], p[2], p[0])
    elif rot == 9: # (-z, +y, +x)
        return (-p[2], p[1], p[0])
    elif rot == 10: # (-y, -z, +x)
        return (-p[1], -p[2], p[0])
    elif rot == 11: # (+z, -y, +x)
        return (p[2], -p[1], p[0])
    # Facing -x dir
    elif rot == 12: # (+z, +y, -x)
        return (p[2], p[1], -p[0])
    elif rot == 13: # (-y, +z, -x)
        return (-p[1], p[2], -p[0])
    elif rot == 14: # (-z, -y, -x)
        return (-p[2], -p[1], -p[0])
    elif rot == 15: # (+y, -z, -x)
        return (p[1], -p[2], -p[0])
    # Facing +y dir
    elif rot == 16: # (+z, +x, +y)
        return (p[2], p[0], p[1])
    elif rot == 17: # (-x, +z, +y)
        return (-p[0], p[2], p[1])
    elif rot == 18: # (-z, -x, +y)
        return (-p[2], -p[0], p[1])
    elif rot == 19: # (+x, -z, +y)
        return (p[0], -p[2], p[1])
    # Facing -y dir
    elif rot == 20: # (+x, +z, -y)
        return (p[0], p[2], -p[1])
    elif rot == 21: # (-z, +x, -y)
        return (-p[2], p[0], -p[1])
    elif rot == 22: # (-x, -z, -y)
        return (-p[0], -p[2], -p[1])
    elif rot == 23: # (+z, -x, -y)
        return (p[2], -p[0], -p[1])

def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2])

def sub(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2])

def attempt(i, j, scanners, conns, offsets):
    # s1 stays fixed, while s2 rotates around by d
    s1 = scanners[i]
    s2 = scanners[j]
    points1 = set(s1)
    for p1 in s1:
        for r in range(numRots):
            for p2 in s2:
            # incorporate failures later
                p2 = rotate(p2, r)
                # offset + rot(s2) = s1
                offset = sub(p1, p2)
                matches = 0
                for p in s2:
                    newP = add(rotate(p, r), offset)
                    if newP in points1:
                        matches += 1
                    if matches >= 12:
                        conns[i].append(j)
                        conns[j].append(i)
                        offsets[(i, j)] = (r, offset)
                        return

def main():
    f = open("tests/test.txt")

    scanners = []
    curScanner = None
    for line in f:
        if len(line) > 1:
            if line[4] == 's':
                if curScanner is not None:
                    scanners.append(curScanner)
                curScanner = []
            elif len(line) > 1:
                coord = line.rstrip().split(",")
                curScanner.append(tuple([int(coord[i]) for i in range(len(coord))]))
    scanners.append(curScanner)

    connected = [[] for _ in range(len(scanners))]
    # For pair of scanners (i, j), it records the (rot, offset) needed to get
    # from j to i, and i will always be less than j
    offsets = {}
    for i in range(len(scanners)):
        for j in range(i + 1, len(scanners)):
            attempt(i, j, scanners, connected, offsets)
    
    pp.pprint(connected)
    pp.pprint(offsets)

    # Adding points (make sure to edit the scanners points as you go)
    added = [False for _ in range(len(scanners))]
    beacons = set() # Scanner 0 is at (0, 0, 0)
    edgesAdded = {}
    toAdd = [(0, 0)]
    added[0] = True
    while len(toAdd) > 0:
        (prev, cur) = toAdd.pop(0)
        pp.pprint((prev, cur))
        if cur == 0:
            for p in scanners[0]:
                beacons.add(p)
        else:
            for i in range(len(scanners[cur])):
                newP = None
                # if prev < cur:
                #     (r, off) = offsets[(prev, cur)]
                #     newP = add(rotate(scanners[cur][i], r), off)
                # else:
                #     (r, off) = offsets[(cur, prev)]
                #     # we know r(prev) + off = cur, so r^{-1}(cur - off) = prev
                #     newP = rotate(sub(scanners[cur][i], off), r)
                #     newP = (-newP[0], -newP[1], -newP[2])
                scanners[cur][i] = newP
                beacons.add(newP)
            pp.pprint(scanners[cur])
        for neigh in connected[cur]:
            if not added[neigh]:
                added[neigh] = True
                toAdd.append((cur, neigh))

    print("Answer: " + str(len(beacons)))
    f.close()

if __name__ ==  "__main__":
    main()