import pprint
import math

pp = pprint.PrettyPrinter()

# requires dx > 0, yH < 0
def simulate(dx, dy, xL, xH, yL, yH):
    start = [0, 0]
    while True:
        if start[0] > xH or start[1] < yL:
            return False
        if xL <= start[0] and start[0] <= xH and yL <= start[1] and start[1] <= yH:
            return True
        start[0] += dx
        start[1] += dy
        dy -= 1
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1

def main():
    f = open("target.txt")

    line = f.readline().rstrip()
    toks = line.split("=")
    xs = toks[1]
    ys = toks[2]

    xL = int(xs.split("..")[0])
    xH = int(xs.split("..")[1].split(",")[0])

    yL = int(ys.split("..")[0])
    yH = int(ys.split("..")[1])

    ans = 0
    dyMin = yL
    dyMax = abs(yL) + 1
    # want (dxMin)(dxMin + 1) / 2 >= xL
    # dxMin^2 + dxMin - 2xL >= 0
    dxMin = math.ceil((-1 + math.sqrt(1 + 8 * xL)) / 2)
    dxMax = xH + 1
    for dy in range(dyMin, dyMax):
        for dx in range(dxMin, dxMax):
            if simulate(dx, dy, xL, xH, yL, yH):
                # pp.pprint((dx, dy))
                ans += 1

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()