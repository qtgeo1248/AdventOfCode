from collections import defaultdict
import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def toBinary(rows):
    newRows = []
    for row in rows:
        cur = 0
        power = 1
        for c in row:
            cur += power * (1 if c == "#" else 0)
            power *= 2
        newRows.append(cur)
    return newRows

def pows(n):
    return set([1 << i for i in range(n)])

def reflection(rows, pow2s):
    for poss in range(len(rows) - 1):
        foundDiff = False
        valid = True
        toLook = range(poss + 1) if poss < len(rows) // 2 else range(poss + 1, len(rows))
        for i in toLook:
            diff = rows[2 * poss - i + 1] ^ rows[i]
            if diff in pow2s:
                if foundDiff:
                    valid = False
                else:
                    foundDiff = True
            elif diff != 0:
                valid = False
        if valid and foundDiff:
            return poss + 1
    return 0

def main():
    f = open("mirrors.txt")

    notes = 0
    lava = []
    for line in f:
        if line == "\n":
            notes += 100 * reflection(toBinary(lava), pows(len(lava[0])))
            cols = [[] for _ in lava[0]]
            for i in range(len(lava)):
                for j in range(len(lava[i])):
                    cols[j].append(lava[i][j])
            notes += reflection(toBinary(cols), pows(len(lava)))
            lava = []
        else:
            lava.append([c for c in line.rstrip()])
    pp.pprint(notes)

if __name__ == "__main__":
    main()
