import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

diffs = {
    '.': {},
    '|': {(-1, 0), (1, 0)},
    '-': {(0, -1), (0, 1)},
    'L': {(-1, 0), (0, 1)},
    'J': {(-1, 0), (0, -1)},
    '7': {(0, -1), (1, 0)},
    'F': {(1, 0), (0, 1)}
}

def findStartPipe(start, pipes):
    posDirs = set()
    for dir in dirs:
        pos = (start[0] + dir[0], start[1] + dir[1])
        if pos[0] < 0 or pos[0] >= len(pipes) or pos[1] < 0 or pos[1] >= len(pipes[0]):
            continue
        for newDir in diffs[pipes[pos[0]][pos[1]]]:
            newPos = (pos[0] + newDir[0], pos[1] + newDir[1])
            if newPos == start:
                posDirs.add(dir)
    for pipe in diffs.keys():
        if posDirs == diffs[pipe]:
            pipes[start[0]][start[1]] = pipe

def findLoop(start, pipes):
    dir = list(diffs[pipes[start[0]][start[1]]])[0]
    pos = (start[0] + dir[0], start[1] + dir[1])
    loop = set()
    loop.add(start)
    loop.add(pos)
    while pos != start:
        actualNext = None
        for dir in diffs[pipes[pos[0]][pos[1]]]:
            nex = (pos[0] + dir[0], pos[1] + dir[1])
            if nex not in loop:
                loop.add(nex)
                actualNext = nex
            if nex == start:
                loop.add(nex)
                actualNext = nex
        pos = actualNext
    return loop

def findEnclosed(pipes, loop):
    matching = {'L': '7', 'F': 'J'}
    numEnclosed = 0
    for i in range(len(pipes)):
        loopSeen = 0
        prevCorner = None
        for j in range(len(pipes[i])):
            if (i, j) not in loop:
                if loopSeen % 2 == 1:
                    # print((i, j))
                    numEnclosed += 1
            elif pipes[i][j] == '|':
                loopSeen += 1
            elif pipes[i][j] in {'L', 'F'}:
                prevCorner = pipes[i][j]
            elif pipes[i][j] in {'7', 'J'}:
                if matching[prevCorner] == pipes[i][j]:
                    loopSeen += 1
    return numEnclosed

def main():
    f = open("pipes.txt")

    pipes = []
    start = None
    for line in f:
        row = []
        for c in line.rstrip():
            if c == 'S':
                start = (len(pipes), len(row))
            row.append(c)
        pipes.append(row)
    findStartPipe(start, pipes)
    loop = findLoop(start, pipes)
    print(findEnclosed(pipes, loop))

if __name__ == "__main__":
    main()
