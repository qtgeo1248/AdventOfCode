import pprint

pp = pprint.PrettyPrinter()

dirs = [
    (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)
]

def isOut(coord, bounds):
    for i in range(len(bounds)):
        if coord[i] < bounds[i][0] - 1 or coord[i] > bounds[i][1] + 1:
            return True
    return False

def findOutside(coord, outside, cubes, bounds):
    frontier = [coord]
    outside.add(coord)
    while len(frontier) > 0:
        cur = frontier.pop()
        for dir in dirs:
            nex = (cur[0] + dir[0], cur[1] + dir[1], cur[2] + dir[2])
            if not isOut(nex, bounds) and nex not in outside and nex not in cubes:
                outside.add(nex)
                frontier.append(nex)

def main():
    f = open("lava.txt")

    cubes = set()

    for line in f:
        cube = line.strip().split(",")
        cubes.add((int(cube[0]), int(cube[1]), int(cube[2])))

    bounds = [[None, None] for _ in range(3)]
    for cube in cubes:
        for i in range(len(bounds)):
            bounds[i][0] = cube[i] if bounds[i][0] is None or cube[i] < bounds[i][0] else bounds[i][0]
            bounds[i][1] = cube[i] if bounds[i][1] is None or cube[i] > bounds[i][1] else bounds[i][1]

    outside = set()
    findOutside((bounds[0][0] - 1, bounds[1][0] - 1, bounds[2][0] - 1), outside, cubes, bounds)
    area = 0
    for cube in cubes:
        for dir in dirs:
            nex = (cube[0] + dir[0], cube[1] + dir[1], cube[2] + dir[2])
            if nex not in cubes and nex in outside:
                area += 1
    print(area)

if __name__ == "__main__":
    main()
