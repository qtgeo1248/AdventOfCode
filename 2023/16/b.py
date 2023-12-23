import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

#             right       down        left         up   
dirToDelta = {0 : (0, 1), 1 : (1, 0), 2 : (0, -1), 3 : (-1, 0)}

def search(start, startDir, grid):
    litup = set()
    seen = set()
    toSearch = [(start, startDir)]

    while len(toSearch) > 0:
        (pos, dir) = toSearch.pop()
        if (pos, dir) in seen or pos[0] < 0 or pos[1] < 0 or pos[0] >= len(grid) or pos[1] >= len(grid[0]):
            continue
        litup.add(pos)
        seen.add((pos, dir))

        newDirs = []
        if grid[pos[0]][pos[1]] == '.':
            newDirs.append(dir)
        elif grid[pos[0]][pos[1]] == '/':
            newDirs.append({0 : 3, 3 : 0, 1 : 2, 2 : 1}[dir])
        elif grid[pos[0]][pos[1]] == '\\':
            newDirs.append({0 : 1, 1 : 0, 2 : 3, 3 : 2}[dir])
        elif grid[pos[0]][pos[1]] == '-':
            if dir % 2 == 0:
                newDirs.append(dir)
            else:
                newDirs.extend([0, 2])
        elif grid[pos[0]][pos[1]] == '|':
            if dir % 2 == 1:
                newDirs.append(dir)
            else:
                newDirs.extend([1, 3])
        for newDir in newDirs:
            delta = dirToDelta[newDir]
            toSearch.append(((pos[0] + delta[0], pos[1] + delta[1]), newDir))
    return len(litup)
    

def main():
    f = open("grid.txt")

    grid = []
    for line in f:
        grid.append([c for c in line.rstrip()])

    maxTiles = 0
    for i in range(len(grid)):
        maxTiles = max(maxTiles, search((i, 0), 0, grid))
        maxTiles = max(maxTiles, search((i, len(grid[i]) - 1), 2, grid))
    for j in range(len(grid[0])):
        maxTiles = max(maxTiles, search((0, j), 1, grid))
        maxTiles = max(maxTiles, search((len(grid) - 1, j), 3, grid))
    pp.pprint(maxTiles)

if __name__ == "__main__":
    main()
