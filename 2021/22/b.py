import pprint

pp = pprint.PrettyPrinter()

def getLastSame(arr, i):
    j = i + 1
    while j < len(arr):
        if arr[i] != arr[j]:
            return j - 1
        j += 1
    return len(arr) - 1

def getCubes(dividers):
    cubes = []
    for xi in dividers:
        ranges = []
        xi.sort()
        j = 0
        while j < len(xi) - 1:
            k = getLastSame(xi, j)
            if j != k:
                xi[k] += 1
                k -= 1
            ranges.append((xi[j], xi[k + 1] - 1))
            j = k + 1
        # Since we never add the last cube, we need to do it here
        ranges.append((xi[len(xi) - 1], xi[len(xi) - 1]))
        cubes.append(ranges)
    return cubes

def binSearch(xi, x, idx):
    lo = 0
    hi = len(xi)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if xi[mid][idx] == x:
            return mid
        if xi[mid][idx] < x:
            lo = mid+1
        else:
            hi = mid
    return None

def doSteps(steps, cubes, isOn):
    step = 0
    for (toggle, coords) in steps:
        idxs = [[binSearch(cubes[i], coords[i][j], j) for j in range(2)] for i in range(3)]
        for i in range(idxs[0][0], idxs[0][1] + 1):
            for j in range(idxs[1][0], idxs[1][1] + 1):
                for k in range(idxs[2][0], idxs[2][1] + 1):
                    isOn[i][j][k] = toggle
        step += 1

def vol(curRange):
    vol = 1
    for i in range(len(curRange)):
        vol *= curRange[i][1] - curRange[i][0] + 1
    return vol

def main():
    f = open("steps.txt")
    # Cubes are denoted by their far corners
    steps = []
    dividers = [[], [], []]
    for line in f:
        step = line.rstrip().split(' ')
        toggle = (step[0] == "on")
        coords = step[1].split(",")
        coords = [xi.split("=")[1].split("..") for xi in coords]
        coords = tuple([tuple([int(xij) for xij in xi]) for xi in coords])
        steps.append((toggle, coords))
        for i in range(len(coords)):
            dividers[i].append(coords[i][0])
            # I am unsure as to why i need to add one here, but whatever
            dividers[i].append(coords[i][1] + 1)
    cubes = getCubes(dividers)
    volume = 0
    isOn = [[[False for _ in range(len(cubes[2]))] for _ in range(len(cubes[1]))] for _ in range(len(cubes[0]))]
    doSteps(steps, cubes, isOn)

    for i in range(len(cubes[0])):
        for j in range(len(cubes[1])):
            for k in range(len(cubes[2])):
                if isOn[i][j][k]:
                    volume += vol((cubes[0][i], cubes[1][j], cubes[2][k]))
    print("Answer: " + str(volume))
    f.close()

if __name__ ==  "__main__":
    main()