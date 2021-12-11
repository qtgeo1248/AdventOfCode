import pprint

dirs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

def isInRange(octopi, i, j):
    return 0 <= i and i < len(octopi) and 0 <= j and j < len(octopi[i])

def update(octopi, i, j):
    flashes = 0
    if isInRange(octopi, i, j):
        octopi[i][j][0] += 1
        if octopi[i][j][0] > 9 and octopi[i][j][1]:
            flashes += 1
            octopi[i][j][1] = False
            for (dy, dx) in dirs:
                flashes += update(octopi, i + dy, j + dx)
    return flashes

def reset(octopi):
    for i in range(len(octopi)):
        for j in range(len(octopi[i])):
            if octopi[i][j][0] > 9:
                octopi[i][j][0] = 0
            octopi[i][j][1] = True

def printOctopi(octopi):
    pp = pprint.PrettyPrinter()
    withoutBools = [[octopi[i][j][0] for j in range(len(octopi[i]))] for i in range(len(octopi))]
    pp.pprint(withoutBools)
    print("\n")

def main():
    flashes = 0
    f = open("octopi.txt")
    octopi = []
    for x in f:
        row = []
        for i in range(len(x)):
            if x[i] != '\n':
                row.append([ord(x[i]) - ord('0'), True])
        octopi.append(row)

    for _ in range(100):
        for i in range(len(octopi)):
            for j in range(len(octopi[i])):
                flashes += update(octopi, i, j)
        reset(octopi)
        # printOctopi(octopi)
    
    print("Answer: " + str(flashes))

if __name__ ==  "__main__":
    main()