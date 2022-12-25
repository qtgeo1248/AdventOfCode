import pprint

pp = pprint.PrettyPrinter()
maxC = 50
gridSize = 2 * maxC + 1

def edit(toggle, x, y, z, cubes):
    cubes[x + maxC][y + maxC][z + maxC] = toggle

def main():
    f = open("steps.txt")
    cubes = [[[False for _ in range(gridSize)] for _ in range(gridSize)] for _ in range(gridSize)]
    for line in f:
        step = line.rstrip().split(' ')
        toggle = (step[0] == "on")
        coords = step[1].split(",")
        coords = [xi.split("=")[1].split("..") for xi in coords]
        for xi in coords:
            if int(xi[0]) < -maxC:
                xi[0] = -maxC
            else:
                xi[0] = int(xi[0])
            if maxC < int(xi[1]):
                xi[1] = maxC
            else:
                xi[1] = int(xi[1])
            if maxC < xi[0] or xi[1] < -maxC:
                xi[0] = 0
                xi[1] = -1
        for x in range(coords[0][0], coords[0][1] + 1):
            for y in range(coords[1][0], coords[1][1] + 1):
                for z in range(coords[2][0], coords[2][1] + 1):
                    edit(toggle, x, y, z, cubes)
    
    ans = 0
    for x in range(gridSize):
        for y in range(gridSize):
            for z in range(gridSize):
                if cubes[x][y][z]:
                    ans += 1

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()