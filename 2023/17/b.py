import heapq
import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

dirs = {(0, 1), (1, 0), (0, -1), (-1, 0)}

def isOppo(dir, other):
    if dir is None:
        return False
    return ((dir[0], -dir[1]) == other or (-dir[0], dir[1]) == other) and dir != other

def search(grid):
    # (dist, inarow, pos, curDir)
    pq = [(0, 0, (0, 0), None)]
    dists = dict()
    while len(pq) > 0:
        (dist, inarow, pos, curDir) = heapq.heappop(pq)
        if (pos, inarow, curDir) in dists:
            continue
        dists[(pos, inarow, curDir)] = dist
        for nextDir in dirs:
            if isOppo(curDir, nextDir):
                continue
            nex = (pos[0] + nextDir[0], pos[1] + nextDir[1])
            if not (0 <= nex[0] < len(grid) and 0 <= nex[1] < len(grid[0])):
                continue
            if (inarow == 10 and nextDir == curDir) or (inarow < 4 and nextDir != curDir and curDir is not None):
                continue
            newInaRow = (inarow + 1 if nextDir == curDir else 1)
            heapq.heappush(pq, (dist + grid[nex[0]][nex[1]], newInaRow, nex, nextDir))
    return dists
    
def main():
    f = open("crucibles.txt")

    grid = []
    for line in f:
        grid.append(list(map(int, line.rstrip())))
    dists = search(grid)

    answers = []
    for (key, val) in dists.items():
        if key[0] == (len(grid) - 1, len(grid[0]) - 1):
            answers.append(val)
    # pp.pprint(dists)
    pp.pprint(min(answers))

if __name__ == "__main__":
    main()
