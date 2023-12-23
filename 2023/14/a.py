import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

def weight(rocks):
    n = len(rocks)
    rocks.append(['#' for _ in rocks[0]])
    ans = 0
    for j in range(len(rocks[0])):
        curCube = 0
        gathered = 0
        for i in range(len(rocks)):
            if rocks[i][j] == 'O':
                gathered += 1
            elif rocks[i][j] == '#':
                tot = ((n - curCube) + (n - curCube - gathered + 1)) * gathered // 2
                ans += tot
                curCube = i + 1
                gathered = 0
    return ans

def main():
    f = open("rocks.txt")

    rocks = []
    for line in f:
        rocks.append([c for c in line.rstrip()])
    pp.pprint(weight(rocks))

if __name__ == "__main__":
    main()
