import pprint

def numPaths(graph, node, marked, twice):
    pp = pprint.PrettyPrinter()
    if node == "end":
        return 1
    ans = 0
    for neigh in graph[node]:
        if neigh != "start" and not (neigh in marked and twice):
            newMarked = marked.copy()
            if neigh.islower():
                newMarked.append(neigh)
            ans += numPaths(graph, neigh, newMarked, twice or neigh in marked)
    return ans

def main():
    pp = pprint.PrettyPrinter()
    f = open("cave.txt")

    graph = {}
    for line in f:
        edge = line.rstrip().split("-")
        for i in range(len(edge)):
            if edge[i] not in graph.keys():
                graph[edge[i]] = (edge[not i],)
            else:
                adjList = list(graph[edge[i]])
                adjList.append(edge[not i])
                graph[edge[i]] = tuple(adjList)

    pp.pprint("Answer: " + str(numPaths(graph, "start", ["start"], False)))
    f.close()

if __name__ ==  "__main__":
    main()