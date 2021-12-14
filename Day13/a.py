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
    for line in f:
        words = line.rstrip().split(" ")
        instr = words[2].split("=")
        folds.append((instr[0] == "x", int(instr[1])))

    (isX, coord) = folds[0]
    newDots = set()
    for dot in dots:
        newDots.add((dot[0] - 2 * (dot[0] - coord) * (dot[0] > coord) * isX,
                     dot[1] - 2 * (dot[1] - coord) * (dot[1] > coord) * (not isX)))
    dots = newDots

    print("Answer: " + str(len(dots)))
    f.close()

if __name__ ==  "__main__":
    main()