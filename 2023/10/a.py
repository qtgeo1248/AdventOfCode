import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

diffs = {
    '.': {},
    '|': {(-1, 0), (1, 0)},
    '-': {(0, -1), (0, 1)},
    'L': {(-1, 0), (0, 1)},
    'J': {(-1, 0), (0, -1)},
    '7': {(0, -1), (1, 0)},
    'F': {(1, 0), (0, 1)}
}

def findPipe(start, pipes):
    posDirs = set()
    for dir in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
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
    loop = set()
    dir = list(diffs[pipes[start[0]][start[1]]])[0]
    pos = (start[0] + dir[0], start[1] + dir[1])
    loop.add(start)
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
    findPipe(start, pipes)
    loop = findLoop(start, pipes)
    print(len(loop) // 2)

if __name__ == "__main__":
    main()
