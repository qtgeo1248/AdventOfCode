import pprint

pp = pprint.PrettyPrinter()
steps = 6

# Array of lengths, where the index 0 is the dimension of the outermost
def emptyCube(dims):
    if len(dims) == 0:
        return False
    else:
        return [emptyCube(dims[1:]) for _ in range(dims[0])]

def expand(hypercubes):
    dims = [len(hypercubes[0]) + 2, len(hypercubes[0][0]) + 2, len(hypercubes[0][0][0]) + 2]
    newHyperCubes = []
    newHyperCubes.append(emptyCube(dims))
    for cube in hypercubes:
        newCube = []
        newCube.append(emptyCube(dims[1:]))
        for plane in cube:
            newPlane = []
            newPlane.append(emptyCube(dims[2:]))
            for row in plane:
                newRow = []
                newRow.append(emptyCube(dims[3:]))
                for active in row:
                    newRow.append(active)
                newRow.append(emptyCube(dims[3:]))
                newPlane.append(newRow)
            newPlane.append(emptyCube(dims[2:]))
            newCube.append(newPlane)
        newCube.append(emptyCube(dims[1:]))
        newHyperCubes.append(newCube)
    newHyperCubes.append(emptyCube(dims))
    return newHyperCubes

def getActive(cubes, x, y, z, w):
    if 0 <= x < len(cubes) and 0 <= y < len(cubes[x]) and 0 <= z < len(cubes[x][y]) and 0 <= w < len(cubes[x][y][z]):
        return cubes[x][y][z][w]
    return False

def isActive(cubes, x, y, z, w):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if dx or dy or dz or dw: # Not all 0's
                        count += getActive(cubes, x + dx, y + dy, z + dz, w + dw)
    if cubes[x][y][z][w]:
        return 2 <= count <= 3
    else:
        return count == 3

def main():
    f = open("cubes.txt")

    flat = []
    for line in f:
        row = [c == '#' for c in line.rstrip()]
        flat.append(row)
    cubes = [[flat]]

    for _ in range(steps):
        # x is the outermost coord, then y, then z
        cubes = expand(cubes)
        cubes = [[[[isActive(cubes, x, y, z, w) for w in range(len(cubes[x][y][z]))] for z in range(len(cubes[x][y]))] for y in range(len(cubes[x]))] for x in range(len(cubes))]

    active = 0
    for x in range(len(cubes)):
        for y in range(len(cubes[x])):
            for z in range(len(cubes[x][y])):
                for w in range(len(cubes[x][y][z])):
                    active += cubes[x][y][z][w]

    print("Answer: " + str(active))
    f.close()

if __name__ ==  "__main__":
    main()