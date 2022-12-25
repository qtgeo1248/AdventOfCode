import pprint

pp = pprint.PrettyPrinter()

def vert(trees, i, j, dy):
    cur = 1
    while 0 <= j + cur * dy and j + cur * dy < len(trees[0]):
        if not (trees[i][j + cur * dy] < trees[i][j]):
            return cur
        cur += 1
    return cur - 1

def hor(trees, i, j, dx):
    cur = 1
    while 0 <= i + cur * dx and i + cur * dx < len(trees):
        if not (trees[i + cur * dx][j] < trees[i][j]):
            return cur 
        cur += 1
    return cur - 1

def main():
    f = open("trees.txt")

    trees = []

    for line in f:
        cur = list(line.strip())
        trees.append([int(x) for x in cur])

    maxScore = 0

    for i in range(len(trees)):
        for j in range(len(trees[i])):
            cur = vert(trees, i, j, 1) * vert(trees, i, j, -1)\
                * hor(trees, i, j, 1) * hor(trees, i, j, -1)
            
            maxScore = max(cur, maxScore)

    print(maxScore)

if __name__ == "__main__":
    main()