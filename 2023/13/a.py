import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def reflection(rows):
    for poss in range(len(rows) - 1):
        isRight = True
        if poss < len(rows) // 2:
            for i in range(poss + 1):
                if rows[i] != rows[poss + (poss - i + 1)]:
                    isRight = False
        else: 
            for i in range(poss + 1, len(rows)):
                if rows[i] != rows[poss - (i - poss - 1)]:
                    isRight = False
        if isRight:
            return poss + 1
    return 0

def main():
    f = open("mirrors.txt")

    notes = 0
    lava = []
    for line in f:
        if line == "\n":
            notes += 100 * reflection(lava)
            cols = [[] for _ in lava[0]]
            for i in range(len(lava)):
                for j in range(len(lava[i])):
                    cols[j].append(lava[i][j])
            notes += reflection(cols)
            lava = []
        else:
            lava.append([c for c in line.rstrip()])
    pp.pprint(notes)

if __name__ == "__main__":
    main()
