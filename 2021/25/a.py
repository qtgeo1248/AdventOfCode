import pprint

pp = pprint.PrettyPrinter()

NON = 0
EAS = 1
SOU = 2

# x goes WE, y goes NS
def nextPoint(y, x, isEast, w, h):
    return ((y + (not isEast)) % h, (x + isEast) % w)

# d is either EAS or SOU
def move(sea, d):
    # Move east ones first, and go from left to right so nothing bad happens
    didMove = False
    newSea = [[None for _ in range(len(sea[0]))] for _ in range(len(sea))]
    for y in range(len(sea)):
        for x in range(len(sea[y])):
            if newSea[y][x] is None:
                if sea[y][x] == d:
                    (newY, newX) = nextPoint(y, x, d == EAS, len(sea[y]), len(sea))
                    if sea[newY][newX] == NON:
                        newSea[y][x] = NON
                        newSea[newY][newX] = d
                        didMove = True
                    else:
                        newSea[y][x] = d
                else:
                    newSea[y][x] = sea[y][x]
    
    for y in range(len(sea)):
        for x in range(len(sea[y])):
            sea[y][x] = newSea[y][x]
    return didMove

def main():
    f = open("sea.txt")

    sea = []
    for line in f:
        row = []
        for c in line.rstrip():
            if c == '.':
                row.append(NON)
            elif c == '>':
                row.append(EAS)
            elif c == 'v':
                row.append(SOU)
        sea.append(row)

    t = 0
    didMove = True
    while didMove:
        east = move(sea, EAS)
        south = move(sea, SOU)
        didMove = east or south
        t += 1

    print("Answer: " + str(t))
    f.close()

if __name__ ==  "__main__":
    main()