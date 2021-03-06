import pprint

dirs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

def isInRange(octopi, i, j):
    return 0 <= i and i < len(octopi) and 0 <= j and j < len(octopi[i])

def update(octopi, i, j):
    if isInRange(octopi, i, j):
        octopi[i][j][0] += 1
        if octopi[i][j][0] > 9 and octopi[i][j][1]:
            octopi[i][j][1] = False
            for (dy, dx) in dirs:
                update(octopi, i + dy, j + dx)

def reset(octopi):
    isAll = True
    for i in range(len(octopi)):
        for j in range(len(octopi[i])):
            isAll = isAll and not octopi[i][j][1]
            if octopi[i][j][0] > 9:
                octopi[i][j][0] = 0
            octopi[i][j][1] = True
    return isAll

def printOctopi(octopi):
    pp = pprint.PrettyPrinter()
    withoutBools = [[octopi[i][j][0] for j in range(len(octopi[i]))] for i in range(len(octopi))]
    pp.pprint(withoutBools)
    print("\n")

def main():
    f = open("octopi.txt")
    octopi = []
    for line in f:
        row = []
        for i in range(len(line)):
            if line[i] != '\n':
                row.append([ord(line[i]) - ord('0'), True])
        octopi.append(row)

    step = 0
    flashNotFound = True
    while flashNotFound:
        for i in range(len(octopi)):
            for j in range(len(octopi[i])):
                update(octopi, i, j)
        if reset(octopi):
            flashNotFound = False
        step += 1
        # printOctopi(octopi)
    
    print("Answer: " + str(step))
    f.close()

if __name__ ==  "__main__":
    main()