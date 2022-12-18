import pprint

pp = pprint.PrettyPrinter()

dirs = [
    (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)
]

def main():
    f = open("lava.txt")

    area = 0
    cubes = set()

    for line in f:
        cube = line.strip().split(",")
        cubes.add((int(cube[0]), int(cube[1]), int(cube[2])))

    for cube in cubes:
        for dir in dirs:
            if (cube[0] + dir[0], cube[1] + dir[1], cube[2] + dir[2]) not in cubes:
                area += 1
    print(area)

if __name__ == "__main__":
    main()
