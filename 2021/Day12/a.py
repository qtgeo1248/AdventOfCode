import pprint

def numPaths(graph, node, marked):
    if node == "end":
        return 1
    if node in marked:
        return 0
    ans = 0
    for neigh in graph[node]:
        newMarked = marked.copy()
        if node.islower():
            newMarked.append(node)
        ans += numPaths(graph, neigh, newMarked)
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

    pp.pprint("Answer: " + str(numPaths(graph, "start", [])))
    f.close()

if __name__ ==  "__main__":
    main()