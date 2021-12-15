import pprint
import heapq

steps = 10
pp = pprint.PrettyPrinter()

# PQ has (risk, coord)
def minpath(paths):
    start = (0, 0)
    pq = []

    wid = len(paths[0])
    hei = len(paths)

    visited = [(0, 0)]

    heapq.heappush(pq, (0, start))
    while len(pq) > 0:
        # pp.pprint(pq)
        lowest = heapq.heappop(pq)
        visited.append(lowest[1])
        if lowest[1] == (wid - 1, hei - 1):
            return lowest
        toAdds = []
        if lowest[1][0] < wid - 1:
            newX = lowest[1][0] + 1
            newY = lowest[1][1]
            toAdds.append((newX, newY))
        if lowest[1][1] < hei - 1:
            newX = lowest[1][0]
            newY = lowest[1][1] + 1
            toAdds.append((newX, newY))
        
        for (x, y) in toAdds:
            if (x, y) not in visited:
                curRisk = lowest[0] + paths[y][x]
                matchedRisk = None
                for (pri, (curx, cury)) in pq:
                    if (x, y) == (curx, cury):
                        matchedRisk = pri
                if matchedRisk is None or matchedRisk > curRisk:
                    heapq.heappush(pq, (curRisk, (x, y)))


def main():
    f = open("map.txt")

    paths = []
    for line in f:
        paths.append([ord(c) - ord('0') for c in line.rstrip()])
    # pp.pprint(paths)
    cheapest = minpath(paths)
    print("Answer: " + str(cheapest[0]))
    f.close()

if __name__ ==  "__main__":
    main()