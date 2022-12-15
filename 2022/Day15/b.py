import pprint

pp = pprint.PrettyPrinter()

low = 0
high = 4000000

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def inRange(coord):
    return low <= coord[0] <= high and low <= coord[1] <= high

def getBads(sensor, beacon):
    poss = set()
    dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    maxD = dist(sensor, beacon)
    for d in range(maxD + 1):
        for dir in dirs:
            cur = (sensor[0] + d * dir[0], sensor[1] + (maxD + 1 - d) * dir[1])
            if inRange(cur):
                poss.add(cur)
    # print(len(poss))
    return poss

def isBad(coord, sensors, beacons):
    for i in range(len(sensors)):
        maxD = dist(sensors[i], beacons[i])
        if dist(coord, sensors[i]) <= maxD:
            return False
    return True

def main():
    f = open("beacons.txt")

    sensors = []
    beacons = []

    for line in f:
        [sensor, beacon] = line.strip().split(": ")
        [sx, sy] = sensor.split(", ")
        sensors.append((int(sx.split("=")[1]), int(sy.split("=")[1])))
        [bx, by] = beacon.split(", ")
        beacons.append((int(bx.split("=")[1]), int(by.split("=")[1])))

    poss = set()
    found = False
    for i in range(len(sensors)):
        # print(i)
        poss = getBads(sensors[i], beacons[i])
        for (x, y) in poss:
            if isBad((x, y), sensors, beacons):
                # print((x, y))
                print(4000000 * x + y)
                found = True
                break
        if found:
            break

if __name__ == "__main__":
    main()
