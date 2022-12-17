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

def dfs(start, t, soFar, press, brain):
    if t == 0:
        return 0
    curMax = 0
    soFar.add(start)
    for (v, d) in brain[start]:
        if d < t and v not in soFar:
            curMax = max(curMax, press[v] * (t - d - 1) + dfs(v, t - d - 1, soFar, press, brain))
    soFar.remove(start)
    return curMax

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
    print(dfs("AA", 30, set(), press, brain))

if __name__ == "__main__":
    main()
