import pprint

pp = pprint.PrettyPrinter()
steps = 6

def expand(cubes):
    newCubes = []
    newCubes.append([[False for _ in range(len(cubes[0][0]) + 2)] for _ in range(len(cubes[0]) + 2)])
    for plane in cubes:
        newPlane = []
        newPlane.append([False for _ in range(len(plane[0]) + 2)])
        for row in plane:
            newRow = []
            newRow.append(False)
            for active in row:
                newRow.append(active)
            newRow.append(False)
            newPlane.append(newRow)
        newPlane.append([False for _ in range(len(plane[0]) + 2)])
        newCubes.append(newPlane)
    newCubes.append([[False for _ in range(len(cubes[0][0]) + 2)] for _ in range(len(cubes[0]) + 2)])
    return newCubes

def getActive(cubes, x, y, z):
    if 0 <= x < len(cubes) and 0 <= y < len(cubes[x]) and 0 <= z < len(cubes[x][y]):
        return cubes[x][y][z]
    return False

def isActive(cubes, x, y, z):
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx or dy or dz: # Not all 0's
                    count += getActive(cubes, x + dx, y + dy, z + dz)
    if cubes[x][y][z]:
        return 2 <= count <= 3
    else:
        return count == 3

def main():
    f = open("cubes.txt")

    flat = []
    for line in f:
        row = [c == '#' for c in line.rstrip()]
        flat.append(row)
    cubes = [flat]

    for _ in range(steps):
        # x is the outermost coord, then y, then z
        cubes = expand(cubes)
        cubes = [[[isActive(cubes, x, y, z) for z in range(len(cubes[x][y]))] for y in range(len(cubes[x]))] for x in range(len(cubes))]

    active = 0
    for x in range(len(cubes)):
        for y in range(len(cubes[x])):
            for z in range(len(cubes[x][y])):
                active += cubes[x][y][z]

    print("Answer: " + str(active))
    f.close()

if __name__ ==  "__main__":
    main()