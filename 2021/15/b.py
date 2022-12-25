import pprint
import heapq

steps = 10
pp = pprint.PrettyPrinter()

def nextVal(val, offset):
    return ((val - 1 + offset) % 9) + 1

# PQ has (risk, coord)
def minpath(paths):
    start = (0, 0)
    pq = []

    wid = len(paths[0])
    hei = len(paths)

    # More like unvisited
    visited = []
    for i in range(len(paths)):
        visited.append([True for _ in range(len(paths[i]))])

    heapq.heappush(pq, (0, start))
    while len(pq) > 0:
        # pp.pprint(pq)
        lowest = heapq.heappop(pq)
        if visited[lowest[1][1]][lowest[1][0]]:
            visited[lowest[1][1]][lowest[1][0]] = False
            if lowest[1] == (wid - 1, hei - 1):
                return lowest
            toAdds = []
            if lowest[1][0] > 0:
                toAdds.append((lowest[1][0] - 1, lowest[1][1]))
            if lowest[1][0] < wid - 1:
                toAdds.append((lowest[1][0] + 1, lowest[1][1]))
            if lowest[1][1] > 0:
                toAdds.append((lowest[1][0], lowest[1][1] - 1))
            if lowest[1][1] < hei - 1:
                toAdds.append((lowest[1][0], lowest[1][1] + 1))
            
            for (x, y) in toAdds:
                if visited[y][x]:
                    heapq.heappush(pq, (lowest[0] + paths[y][x], (x, y)))


def main():
    f = open("map.txt")

    ogpaths = []
    for line in f:
        ogpaths.append([ord(c) - ord('0') for c in line.rstrip()])
    # pp.pprint(paths)

    paths = [ogpaths[i].copy() for i in range(len(ogpaths))]
    for j in range(1, 5):
        for i in range(len(paths)):
            paths[i].extend([nextVal(ogpaths[i][cur], j) for cur in range(len(ogpaths[i]))])
    
    for i in range(1, 5):
        for row in range(len(ogpaths)):
            paths.append([nextVal(paths[row][j], i) for j in range(len(paths[row]))])
    # for i in range(len(paths)):
    #     print(paths[i])            


    cheapest = minpath(paths)
    print("Answer: " + str(cheapest[0]))
    f.close()

if __name__ ==  "__main__":
    main()