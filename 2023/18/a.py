import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

def search(border):
    tot = 0
    seen = {(1, 1)}
    frontier = [(1, 1)]
    while len(frontier) > 0:
        pos = frontier.pop()
        tot += 1
        for dir in dirs.values():
            nex = (pos[0] + dir[0], pos[1] + dir[1])
            if nex not in border and nex not in seen:
                seen.add(nex)
                frontier.append(nex)
    return tot + len(border)

def main():
    f = open("digplan.txt")


    minCoords = (0, 0)
    maxCoords = (0, 0)

    cur = (0, 0)
    border = {cur}

    for line in f:
        [dir, n, _] = line.rstrip().split()
        dir = dirs[dir]
        for _ in range(int(n)):
            cur = (cur[0] + dir[0], cur[1] + dir[1])
            border.add(cur)
            maxCoords = (max(maxCoords[0], cur[0]), max(maxCoords[1], cur[1]))
            minCoords = (min(minCoords[0], cur[0]), min(minCoords[1], cur[1]))
        
    pp.pprint(search(border))



if __name__ == "__main__":
    main()
