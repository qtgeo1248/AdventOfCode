import pprint
import math

pp = pprint.PrettyPrinter()

# requires yL <= yH <= 0 <= xL <= xH
def isPossible(dy, xL, xH, yL, yH):
    tFloor = 0 if dy < 0 else 2 * dy + 1
    dy = abs(dy) - 1 if dy <= 0 else dy
    # Want Sum = dy + 1 + dy + 2 + ... + dy + t = (2dy + t + 1)t / 2
    # Equation(s) want to solve is -yH <= (2dy + t + 1)t / 2 <= -yL
    # -2yH <= 2dy*t + t^2 + t <= -2yL
    # t^2 + (2dy + 1)t + 2yH >= 0
    # t^2 + (2dy + 1)t + 2yL <= 0
    tMin = tFloor + math.ceil((-(2 * dy + 1) + math.sqrt((2 * dy + 1) ** 2 - 8 * yH)) / 2)
    tMax = tFloor + math.floor((-(2 * dy + 1) + math.sqrt((2 * dy + 1) ** 2 - 8 * yL)) / 2)
    if tMin > tMax:
        return None

    # want (dxMin)(dxMin + 1) / 2 >= xL
    # dxMin^2 + dxMin - 2xL >= 0
    dxMin = math.ceil((-1 + math.sqrt(1 + 8 * xL)) / 2)
    for dx in range(dxMin, xH + 1):
        # Sum is dx + dx - 1 + ... + dx - tMin of tMin <= dx
        # or dx + dx - 1 + ... + 1 + 0 otherwise (same for tMax)
        xMin = (2 * dx - tMin) * (tMin + 1) / 2 if tMin <= dx else dx * (dx + 1) / 2
        xMax = (2 * dx - tMax) * (tMax + 1) / 2 if tMax <= dx else dx * (dx + 1) / 2
        if xMin <= xH and xL <= xMax:
            return dx
    return None

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

    yMax = 0
    dyMax = abs(yL) + 1
    for dy in range(0, dyMax):
        dx = isPossible(dy, xL, xH, yL, yH)
        if not (dx is None):
            # Sum is 1 + 2 + ... + dy
            height = (dy + 1) * dy // 2
            print("dy: " + str(dy) + " dx: " + str(dx) + " height: " + str(height))
            yMax = height if height > yMax else yMax

    print("Answer: " + str(yMax))
    f.close()

if __name__ ==  "__main__":
    main()