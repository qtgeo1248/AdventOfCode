import pprint

pp = pprint.PrettyPrinter()

alltypes = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)]
]

topMosts = [0, 2, 2, 3, 1]

def move(curRock, rocks, h, jets, i): # Does ####
    start = (2, h)
    def isDone():
        for dir in curRock:
            if (start[0] + dir[0], start[1] + dir[1] - 1) in rocks:
                for dirr in curRock:
                    rocks.add((start[0] + dirr[0], start[1] + dirr[1]))
                return True
        return False
    def canMove(d):
        for dir in curRock:
            pt = (start[0] + dir[0], start[1] + dir[1])
            if pt[0] + d < 0 or pt[0] + d > 6 or (pt[0] + d, pt[1]) in rocks:
                return False
        return True

    notDone = True
    while notDone:
        if jets[i] == "<" and canMove(-1):
            start = (start[0] - 1, start[1])
        if jets[i] == ">" and canMove(1):
            start = (start[0] + 1, start[1])
        if isDone():
            notDone = False
        else:
            start = (start[0], start[1] - 1)
        i = (i + 1) % len(jets)

    return (start[1], i)

def main():
    f = open("jets.txt")

    stream = f.readline().strip()
    rocks = set([(i, 0) for i in range(7)])
    height = 0
    jetI = 0

    for i in range(2022):
        (nexH, jetI) = move(alltypes[i % 5], rocks, height + 4, stream, jetI)
        height = max(height, nexH + topMosts[i % 5])
    print(height)

if __name__ == "__main__":
    main()
