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

def bfs(board, g):
    frontier = [g]
    dist = 0
    visited = set()
    visited.add(g)
    while len(frontier) > 0:
        nextLayer = []
        for u in frontier:
            if board[u[0]][u[1]] == 0:
                return dist
            for d in dirs:
                v = (u[0] + d[0], u[1] + d[1])
                if 0 <= v[0] < len(board) and 0 <= v[1] < len(board[v[0]]):
                    if board[v[0]][v[1]] >= board[u[0]][u[1]] - 1 and v not in visited:
                        visited.add(v)
                        nextLayer.append(v)
        frontier = nextLayer
        dist += 1

def main():
    f = open("heightmap.txt")

    board = []
    goal = None

    for line in f:
        for i in range(len(line)):
            if line[i] == "E":
                goal = (len(board), i)
        board.append([getAscii(c) for c in line.strip()])
    print(bfs(board, goal))

if __name__ == "__main__":
    main()
