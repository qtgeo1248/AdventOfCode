import pprint

pp = pprint.PrettyPrinter()

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def getAscii(c):
    if c == "S":
        return 0
    elif c == "E":
        return ord('z') - ord('a')
    else:
        return ord(c) - ord('a')

def bfs(board, s, g):
    frontier = [s]
    dist = 0
    visited = set()
    visited.add(s)
    while len(frontier) > 0:
        nextLayer = []
        for u in frontier:
            if u == g:
                return dist
            for d in dirs:
                v = (u[0] + d[0], u[1] + d[1])
                if 0 <= v[0] < len(board) and 0 <= v[1] < len(board[v[0]]):
                    if board[v[0]][v[1]] <= board[u[0]][u[1]] + 1 and v not in visited:
                        visited.add(v)
                        nextLayer.append(v)
        frontier = nextLayer
        dist += 1

def main():
    f = open("heightmap.txt")

    board = []
    start = None
    goal = None

    for line in f:
        for i in range(len(line)):
            if line[i] == "S":
                start = (len(board), i)
            if line[i] == "E":
                goal = (len(board), i)
        board.append([getAscii(c) for c in line.strip()])
    print(bfs(board, start, goal))

if __name__ == "__main__":
    main()
