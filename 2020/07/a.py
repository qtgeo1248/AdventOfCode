import pprint

pp = pprint.PrettyPrinter()

def main():
    f = open("rules.txt")

    # Each bag have items that tell you how many of each item you can fit inside the bag
    children = {}
    # Each bag have items that tell you have many of this bag can fit inside the item
    parents = {}
    for line in f:
        rule = line.rstrip().split(" contain ")
        bigBagType = rule[0].split(" bags")[0]
        parents[bigBagType] = tuple()
        contain = []
        bags = rule[1].split(", ")
        for bag in bags:
            numIdx = bag.find(' ')
            num = bag[0:numIdx]
            if num.isdigit():
                bagType = (bag[numIdx + 1:]).split(" bag")[0]
                contain.append((bagType, int(num)))
        children[bigBagType] = tuple(contain)
    for (big, smallBags) in children.items():
        for (small, n) in smallBags:
            curParents = list(parents[small])
            curParents.append((big, n))
            parents[small] = tuple(curParents)
    # pp.pprint(children)
    # pp.pprint(parents)

    visited = set()
    toAdd = ["shiny gold"]
    while len(toAdd) > 0:
        bag = toAdd.pop(0)
        if bag in parents:
            for (neigh, _) in parents[bag]:
                if neigh not in visited:
                    visited.add(neigh)
                    toAdd.append(neigh)
    print("Answer: " + str(len(visited)))
    f.close()

if __name__ ==  "__main__":
    main()