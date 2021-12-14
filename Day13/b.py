import pprint

def main():
    pp = pprint.PrettyPrinter()
    f = open("polymer.txt")

    dots = set()
    readDots = True
    while readDots:
        line = f.readline().rstrip()
        if len(line) == 0:
            readDots = False
        else:
            dot = line.split(",")
            dots.add((int(dot[0]), int(dot[1])))
    folds = []
    xMin = None
    yMin = None
    for line in f:
        words = line.rstrip().split(" ")
        instr = words[2].split("=")
        coord = int(instr[1])
        isX = instr[0] == "x"
        folds.append((isX, coord))
        xMin = coord if isX and (xMin is None or xMin > coord) else xMin
        yMin = coord if not isX and (yMin is None or yMin > coord) else yMin

    for (isX, coord) in folds:
        newDots = set()
        for dot in dots:
            newDots.add((dot[0] - 2 * (dot[0] - coord) * (dot[0] > coord) * isX,
                        dot[1] - 2 * (dot[1] - coord) * (dot[1] > coord) * (not isX)))
        dots = newDots

    pp.pprint((xMin, yMin))
    gridArr = []
    for _ in range(yMin):
        row = []
        for _ in range(xMin):
            row.append(False)
        gridArr.append(row)
    for dot in dots:
        gridArr[dot[1]][dot[0]] = True

    for i in range(len(gridArr)):
        row = ""
        for j in range(len(gridArr[i])):
            row += "#" if gridArr[i][j] else "."
        pp.pprint(row)
    
    f.close()

if __name__ ==  "__main__":
    main()