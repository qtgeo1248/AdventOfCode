import pprint

pp = pprint.PrettyPrinter()

def addStuff(start, end, stuff):
    start = (int(start[0]), int(start[1]))
    end = (int(end[0]), int(end[1]))
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    if dx == 0:
        isNeg = 1 if dy > 0 else -1
        for i in range(abs(dy) + 1):
            stuff.add((start[0], start[1] + i * isNeg))
    else:
        isNeg = 1 if dx > 0 else -1
        for i in range(abs(dx) + 1):
            stuff.add((start[0] + i * isNeg, start[1]))
    return max(start[1], start[1] + dy)

def addSand(stuff, noReturn):
    sand = (500, 0)
    while sand[1] < noReturn:
        if (sand[0], sand[1] + 1) not in stuff:
            sand = (sand[0], sand[1] + 1)
        elif (sand[0] - 1, sand[1] + 1) not in stuff:
            sand = (sand[0] - 1, sand[1] + 1)
        elif (sand[0] + 1, sand[1] + 1) not in stuff:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            stuff.add(sand)
            return True
    return False

def main():
    f = open("scan.txt")

    stuff = set()
    noReturn = 0

    for line in f:
        line = line.strip().split(" -> ")
        for i in range(len(line) - 1):
            noReturn = max(noReturn, addStuff(line[i].split(","), line[i + 1].split(","), stuff))

    numSand = 0
    while addSand(stuff, noReturn):
        numSand += 1
    print(numSand)

if __name__ == "__main__":
    main()
