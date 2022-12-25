import pprint

pp = pprint.PrettyPrinter()

def vert(trees, vis, start, dy):
    maxes = [-1 for _ in trees[start]]
    while 0 <= start and start < len(trees):
        for i in range(len(trees[start])):
            if maxes[i] < trees[start][i]:
                vis.add((start, i))
                maxes[i] = trees[start][i]
        start += dy

def hor(trees, vis, start, dx):
    maxes = [-1 for _ in trees]
    while 0 <= start and start < len(trees[0]):
        for i in range(len(trees)):
            if maxes[i] < trees[i][start]:
                vis.add((i, start))
                maxes[i] = trees[i][start]
        start += dx

def main():
    f = open("trees.txt")

    trees = []

    for line in f:
        cur = list(line.strip())
        trees.append([int(x) for x in cur])

    totalVis = set()
    vert(trees, totalVis, 0, 1)
    vert(trees, totalVis, len(trees) - 1, -1)

    hor(trees, totalVis, 0, 1)
    hor(trees, totalVis, len(trees[0]) - 1, -1)

    print(len(totalVis))

if __name__ == "__main__":
    main()