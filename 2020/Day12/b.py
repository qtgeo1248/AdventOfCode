import pprint

pp = pprint.PrettyPrinter()

def rotWaypt(waypt, r, numTimes):
    neg = int(r == 'R') * 2 - 1
    for _ in range(numTimes):
        waypt = [neg * waypt[1], -1 * neg * waypt[0]]
    return waypt

def addWaypt(waypt, d, num):
    if d == 'N' or d == 'S':
        waypt[1] += (int(d == 'N') * 2 - 1) * num
    elif d == 'E' or d == 'W':
        waypt[0] += (int(d == 'E') * 2 - 1) * num

def main():
    f = open("actions.txt")

    coord = [0, 0] # (x, y) coord
    waypoint = [10, 1]
    for line in f:
        act = line[0]
        num = int(line[1:].rstrip())
        if act == 'F':
            for _ in range(num):
                for i in range(len(coord)):
                    coord[i] += waypoint[i]
        elif act == 'R' or act == 'L':
            waypoint = rotWaypt(waypoint, act, num // 90)
        else:
            addWaypt(waypoint, act, num)

    dist = 0
    for xi in coord:
        dist += abs(xi)
    print("Answer: " + str(dist))
    f.close()

if __name__ ==  "__main__":
    main()