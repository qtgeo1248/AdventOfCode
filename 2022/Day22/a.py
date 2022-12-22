import pprint

pp = pprint.PrettyPrinter()

def findBounds(maze, numRows, numCols):
    rowBounds = [None for _ in range(numRows)]
    colBounds = [None for _ in range(numCols)]
    for i in range(numRows):
        left = 0
        right = len(maze[i]) - 1
        while maze[i][left] == " ":
            left += 1
        while right >= len(maze[i]) or maze[i][right] == " ":
            right -= 1
        rowBounds[i] = (left, right)
    for j in range(numCols):
        top = 0
        bot = numRows - 1
        while j >= len(maze[top]) or maze[top][j] == " ":
            top += 1
        while j >= len(maze[bot]) or maze[bot][j] == " ":
            bot -= 1
        colBounds[j] = (top, bot)
    return rowBounds, colBounds

def findWalls(maze):
    walls = set()
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "#":
                walls.add((i, j))
    return walls

def outRow(coord, rowBounds):
    if coord[1] < rowBounds[coord[0]][0]:
        return (coord[0], rowBounds[coord[0]][1])
    if coord[1] > rowBounds[coord[0]][1]:
        return (coord[0], rowBounds[coord[0]][0])
    return coord

def outCol(coord, colBounds):
    if coord[0] < colBounds[coord[1]][0]:
        return (colBounds[coord[1]][1], coord[1])
    if coord[0] > colBounds[coord[1]][1]:
        return (colBounds[coord[1]][0], coord[1])
    return coord

def follow(walls, rowBounds, colBounds, path):
    start = (0, rowBounds[0][0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dirIdx = 0
    pathIdx = 0
    while pathIdx < len(path):
        if path[pathIdx] == "R":
            dirIdx = (dirIdx + 1) % 4
            pathIdx += 1
        elif path[pathIdx] == "L":
            dirIdx = (dirIdx - 1) % 4
            pathIdx += 1
        else:
            toMove = 0
            while pathIdx < len(path) and path[pathIdx].isdigit():
                toMove = 10 * toMove + int(path[pathIdx])
                pathIdx += 1
            for _ in range(toMove):
                nex = (start[0] + dirs[dirIdx][0], start[1] + dirs[dirIdx][1])
                if dirs[dirIdx][0] != 0:
                    nex = outCol(nex, colBounds)
                else:
                    nex = outRow(nex, rowBounds)
                if nex in walls:
                    break
                start = nex
    return start, dirIdx

def main():
    f = open("field.txt")

    maze = []
    numCols = 0
    numRows = 0
    isMaze = True
    path = None
    for line in f:
        if line == "\n":
            isMaze = False
        elif isMaze:
            maze.append(line[:-1])
            numRows += 1
            numCols = max(numCols, len(maze[-1]))
        else:
            path = line.strip()
    rowBounds, colBounds = findBounds(maze, numRows, numCols)
    # print(rowBounds)
    # print(colBounds)
    walls = findWalls(maze)

    final, dirIdx = follow(walls, rowBounds, colBounds, path)
    print(1000 * (final[0] + 1) + 4 * (final[1] + 1) + dirIdx)


if __name__ == "__main__":
    main()
