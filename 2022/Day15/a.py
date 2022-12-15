import pprint

pp = pprint.PrettyPrinter()

rowWant = 2000000

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def addImps(sensors, beacons):
    ans = []
    for i in range(len(sensors)):
        maxD = dist(sensors[i], beacons[i])
        dy = abs(sensors[i][1] - rowWant) # Change later
        dx = maxD - dy
        if dx >= 0:
            if rowWant == beacons[i][1]:
                if dx > 0:
                    if beacons[i][0] == sensors[i][0] - dx:
                        ans.append((sensors[i][0] - dx + 1, sensors[i][0] + dx))
                    else:
                        ans.append((sensors[i][0] - dx, sensors[i][0] + dx - 1))
            else:
                ans.append((sensors[i][0] - dx, sensors[i][0] + dx))
    return ans

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
    
    imps = addImps(sensors, beacons)
    imps.sort(key=lambda x: x[0])
    print(imps)

    prevEnd = imps[0][1]
    ans = imps[0][1] - imps[0][0] + 1
    for i in range(1, len(imps)):
        if prevEnd < imps[i][0]:
            ans += imps[i][1] - imps[i][0] + 1
            prevEnd = imps[i][1]
        elif prevEnd < imps[i][1]:
            ans += imps[i][1] - prevEnd
            prevEnd = imps[i][1]
    print(ans)

if __name__ == "__main__":
    main()
