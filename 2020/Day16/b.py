import pprint

pp = pprint.PrettyPrinter()

def validOne(n, rule):
    for r in rule:
        if r[0] <= n <= r[1]:
            return True
    return False

def validAll(n, rules):
    for rule in rules.values():
        if validOne(n, rule):
            return True
    return False

def deduce(poss, names, positions):
    didChange = False
    for i in range(len(names)):
        if len(poss[i]) == 1:
            loc = list(poss[i])[0]
            positions[loc] = names[i]
            for s in poss:
                if loc in s:
                    s.remove(loc)
            didChange = True
    return didChange

def main():
    f = open("tickets.txt")
    numNewLines = 0
    rules = {}
    mine = None
    nearby = []
    names = []
    for line in f:
        if line == "\n":
            numNewLines += 1
            f.readline()
        elif numNewLines == 0: # Rules
            rule = line.rstrip().split(": ")
            curRange = rule[1].split(" or ")
            curRange = [cur.split("-") for cur in curRange]
            curRange = tuple([tuple([int(c) for c in cur]) for cur in curRange])
            rules[rule[0]] = curRange
            names.append(rule[0])
        elif numNewLines == 1: # Your ticket
            mine = line.rstrip().split(",")
            mine = tuple([int(n) for n in mine])
        else: # Nearby tickets
            nums = line.rstrip().split(",")
            nums = [int(n) for n in nums]
            toAdd = True
            for n in nums:
                if not validAll(n, rules):
                    toAdd = False
            if toAdd:
                nearby.append(tuple(nums))

    poss = [set(range(0, len(mine))) for _ in range(len(names))]
    for ticket in nearby:
        for i in range(len(ticket)):
            for r in range(len(names)):
                if not validOne(ticket[i], rules[names[r]]):
                    poss[r].remove(i)
    positions = {}
    while deduce(poss, names, positions):
        positions
    
    ans = 1
    for (i, rule) in positions.items():
        if rule.split(" ")[0] == "departure":
            ans *= mine[i]

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()