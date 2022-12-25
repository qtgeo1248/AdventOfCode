import pprint

pp = pprint.PrettyPrinter()

totMin = 30

def getBranches(start, neighs, press, brain):
    d = 0
    brain[start] = []
    visited = set([start])
    frontier = [start]
    while len(frontier) > 0:
        newFront = []
        for u in frontier:
            if press[u] > 0 and u != start:
                brain[start].append((u, d))
            for v in neighs[u]:
                if v not in visited:
                    visited.add(v)
                    newFront.append(v)
        frontier = newFront
        d += 1

def dfs(start, t, soFar, wants, press, brain):
    if t == 0:
        return 0
    curMax = 0
    soFar.add(start)
    for (v, d) in brain[start]:
        if d < t and v not in soFar and v in wants:
            curMax = max(curMax, press[v] * (t - d - 1) + dfs(v, t - d - 1, soFar, wants, press, brain))
    soFar.remove(start)
    return curMax

def trySubsets(allNonNeg, i, me, ele, press, brain):
    if i == len(allNonNeg):
        return dfs("AA", 26, set(), me, press, brain) + dfs("AA", 26, set(), ele, press, brain)
    else:
        me.add(allNonNeg[i])
        first = trySubsets(allNonNeg, i + 1, me, ele, press, brain)
        me.remove(allNonNeg[i])
        ele.add(allNonNeg[i])
        second = trySubsets(allNonNeg, i + 1, me, ele, press, brain)
        ele.remove(allNonNeg[i])
        return max(first, second)


def main():
    f = open("report.txt")

    neighs = dict()
    press = dict()

    for line in f:
        [p, ns] = line.strip().split("; ")
        p = p.split(" ")
        press[p[1]] = int(p[4].split("=")[1])
        ns = ns.split(", ")
        ns[0] = ns[0].split(" ")[-1]
        neighs[p[1]] = ns
    
    brain = dict()
    for (valves, pr) in press.items():
        if valves == "AA" or pr > 0:
            getBranches(valves, neighs, press, brain)

    allNonNeg = []
    for (v, p) in press.items():
        if p > 0:
            allNonNeg.append(v)
    print(trySubsets(allNonNeg, 0, set(), set(), press, brain))

if __name__ == "__main__":
    main()
