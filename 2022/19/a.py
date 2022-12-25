import pprint

pp = pprint.PrettyPrinter()

def addTime(ores, robots, t):
    for typ in ores:
        ores[typ] += t * robots[typ]

def doRobot(ores, blue, rob, toDo):
    for (typ, co) in blue[rob]:
        ores[typ] -= co * toDo

def shouldDo(robots, blue):
    should = set(["geode"])
    for (_, costs) in blue.items():
        for (typ, co) in costs:
            if co > robots[typ]:
                should.add(typ)
    return should

def getNumGeos(blue, t, robots, ores, brain):
    key = (tuple(robots.items()), t, tuple(ores.items()))
    if t == 0:
        return ores["geode"]
    if key in brain:
        return brain[key]
    curMax = 0
    for rob in shouldDo(robots, blue):
        maxT = 0
        for (typ, co) in blue[rob]:
            if robots[typ] == 0:
                maxT = None
                break
            maxT = max(maxT, (co - ores[typ] - 1) // robots[typ] + 1)
        ub = ores["geode"] + robots["geode"] * t + t * (t - 1) // 2
        if maxT is not None and maxT + 1 <= t and ub > curMax:
            addTime(ores, robots, maxT + 1)
            doRobot(ores, blue, rob, 1)
            robots[rob] += 1
            curMax = max(curMax, getNumGeos(blue, t - maxT - 1, robots, ores, brain))
            robots[rob] -= 1
            doRobot(ores, blue, rob, -1)
            addTime(ores, robots, -(maxT + 1))
    # Try not doing anything
    addTime(ores, robots, t)
    curMax = max(curMax, getNumGeos(blue, 0, robots, ores, brain))
    addTime(ores, robots, -t)
    brain[key] = curMax
    return curMax

def main():
    f = open("blueprints.txt")

    blueprints = []
    allOres = []

    for line in f:
        costs = line.strip()[:-1].split(": ")[1].split(". ")
        curBlue = dict()
        for robot in costs:
            curCosts = []
            typ = robot.split("Each ")[1].split(" robot")[0]
            allOres.append(typ)
            cost = robot.split("costs ")[1].split(" and ")
            for ing in cost:
                ing = ing.split(" ")
                curCosts.append((ing[1], int(ing[0])))
            curBlue[typ] = curCosts
        blueprints.append(curBlue)

    tot = 0
    for i in range(len(blueprints)):
        blue = blueprints[i]
        ores = dict()
        robos = dict()
        for typ in allOres:
            ores[typ] = 0
            robos[typ] = 0
        robos["ore"] = 1
        tot += (i + 1) * getNumGeos(blue, 24, robos, ores, dict())
    print(tot)

if __name__ == "__main__":
    main()
