import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def decodeHex(line):
    [_, _, hexadec] = line.rstrip().split()
    num = hexadec[2:7]
    last = hexadec[7]
    return (dirs[int(last)], int(num, 16))

def search(border, rows, cols):
    tot = 0
    # start hardcoded
    start = (rows.index(1), cols.index(1))
    seen = {start}
    frontier = [start]
    while len(frontier) > 0:
        pos = frontier.pop()
        actual = (rows[pos[0]], cols[pos[1]])
        tot += (rows[pos[0] + 1] - actual[0]) * (cols[pos[1] + 1] - actual[1])
        for dir in dirs:
            nex = (pos[0] + dir[0], pos[1] + dir[1])
            if nex not in border and nex not in seen:
                seen.add(nex)
                frontier.append(nex)
    return tot

def main():
    f = open("digplan.txt")

    rows = set()
    cols = set()
    cur = (0, 0)
    lenBorder = 0

    plan = []

    for line in f:
        (dir, n) = decodeHex(line)
        plan.append((dir, n))
        cur = (cur[0] + n * dir[0], cur[1] + n * dir[1])
        rows.update({cur[0] - 1, cur[0], cur[0] + 1})
        cols.update({cur[1] - 1, cur[1], cur[1] + 1})
        lenBorder += n * abs(dir[0]) + n * abs(dir[1])

    rows = sorted(rows)
    cols = sorted(cols)

    newCur = (rows.index(0), cols.index(0))
    actual = (rows[newCur[0]], cols[newCur[1]])
    border = {newCur}

    for (dir, n) in plan:
        target = (actual[0] + n * dir[0], actual[1] + n * dir[1])
        while actual != target:
            newCur = (newCur[0] + dir[0], newCur[1] + dir[1])
            actual = (rows[newCur[0]], cols[newCur[1]])
            border.add(newCur)
    interior = search(border, rows, cols)
    pp.pprint(interior + lenBorder)

if __name__ == "__main__":
    main()
