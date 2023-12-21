import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

expansion = 1000000

def main():
    f = open("space.txt")

    rows = []
    for line in f:
        rows.append(list(line.rstrip()))
    cols = [[] for _ in range(len(rows[0]))]
    galaxies = []
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            cols[j].append(rows[i][j])
            if rows[i][j] == '#':
                galaxies.append((i, j))
    rowSpaces = dict()
    colSpaces = dict()
    numSpaces = 0
    for i in range(len(rows)):
        if len(set(rows[i])) == 1:
            numSpaces += 1
        else:
            rowSpaces[i] = numSpaces
    numSpaces = 0
    for j in range(len(cols)):
        if len(set(cols[j])) == 1:
            numSpaces += 1
        else:
            colSpaces[j] = numSpaces

    totDist = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            gal0 = galaxies[i]
            gal1 = galaxies[j]
            dist = abs(gal0[0] - gal1[0]) + abs(gal0[1] - gal1[1])
            dist += (expansion - 1) * (abs(rowSpaces[gal0[0]] - rowSpaces[gal1[0]]) + abs(colSpaces[gal0[1]] - colSpaces[gal1[1]]))
            totDist += dist
    pp.pprint(totDist)

if __name__ == "__main__":
    main()
