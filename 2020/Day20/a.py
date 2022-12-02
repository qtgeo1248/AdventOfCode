import pprint

TOP = 0
LEF = 1
BOT = 2
RIG = 3
numDirs = 4

pp = pprint.PrettyPrinter()

def rot(x, y, r, w):
    if r == TOP:
        return (x, y)
    return rot(y, -(x + 1) % w, r - 1, w)

def attempt(i, j, images):
    A1 = images[i][1]
    A2 = images[j][1]
    for r1 in range(numDirs):
        for r2 in range(numDirs):
            for f2 in range(2): # Should you flip the second one
                isMatch = True
                for d in range(len(A1)): # should be a square
                    (x1, y1) = rot(d, 0, r1, len(A1))
                    (x2, y2) = rot(d if f2 else -(d + 1) % len(A1), 0, r2, len(A1))
                    if A1[y1][x1] != A2[y2][x2]:
                        isMatch = False
                if isMatch:
                    return (r1, r2, f2)
    return None

def newPlace(x, y, top, lastFlip, s1, s2, newFlip):
    realSide = (top + lastFlip * s1) % 4
    newX = x + (realSide - 2) * (realSide % 2)
    newY = y + (realSide - 1) * (not (realSide % 2))

def main():
    f = open("tests/test.txt")
    images = [] 
    camId = None
    curIm = []
    for line in f:
        if line[0] == '\n':
            images.append((camId, curIm))
            camId = None
            curIm = []
        elif line[0] == 'T':
            camId = int(line.split(" ")[1].split(":")[0])
        else:
            curIm.append([c for c in line.rstrip()])
    images.append((camId, curIm))

    # Pairs of (i1, j2), where matches[(i1, i2)] gives you (s1, s2, f), where s1
    # and s2 are in {TOP, LEFT, RIGHT, BOT} of telling where they match, f is
    # whether you should flip the second image by the side where it matches
    matches = {}
    matched = set()
    matched.add(0)
    frontier = [0]
    while len(frontier) > 0:
        cur = frontier.pop(0)
        for j in range(len(images)):
            if j not in matched:
                res = attempt(cur, j, images)
                if res is not None:
                    matches[(cur, j)] = res
                    matched.add(j)
                    frontier.append(j)
    # pp.pprint(matches)

    # places[(x, y)] is the coordinates, and it returns the ID there
    places = {}
    places[(0, 0)] = images[0][0]
    placed = set()
    placed.add(0)
    # (idx, (lastX, lastY, whereIsTop, rotation /* either 1 (CClock) or -1 (Clock) */))
    frontier = [(0, (0, 0, TOP, 1))]
    while len(frontier) > 0:
        (cur, (x, y, top, lastFlip)) = frontier.pop(0)
        for j in range(len(images)):
            if (cur, j) in matches.keys() and j not in placed:
                (s1, s2, newFlip) = matches[(cur, j)]
                (newX, newY, newTop, newFlip) = newPlace(x, y, top, lastFlip, s1, s2, newFlip)
                places[(newX, newY)] = images[j][0]
                placed.add(j)
                frontier.append((j, (newX, newY, newTop, newFlip)))

    print("Answer: ")
    f.close()

if __name__ ==  "__main__":
    main()