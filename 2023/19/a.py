import pprint

pp = pprint.PrettyPrinter(width=150)

# line = f.readline().rstrip()

class WorkFlow:
    def __init__(self, line):
        [name, rest] = line.rstrip().split("{")
        self.name = name
        rawRules = rest[:-1].split(",")
        # (is>Sign, xmas, bound, next)
        self.rules = []
        for rawRule in rawRules:
            parsed = rawRule.split(":")
            if len(parsed) == 1:
                self.end = parsed[0]
            elif parsed[0][1] == "<":
                rule = parsed[0].split("<")
                self.rules.append((True, rule[0], int(rule[1]), parsed[1]))
            else: 
                rule = parsed[0].split(">")
                self.rules.append((False, rule[0], int(rule[1]), parsed[1]))
    
    def next(self, part):
        for rule in self.rules:
            if rule[0] and part[rule[1]] < rule[2]:
                return rule[3]
            elif not rule[0] and part[rule[1]] > rule[2]:
                return rule[3]
        return self.end

    def __repr__(self):
        return str((self.name, self.rules))

def main():
    f = open("parts.txt")

    workflows = dict()
    partRatings = []

    for line in f:
        if line[0] == "{":
            partsRaw = line[1:-2].split(",")
            parts = map(lambda part: part.split("="), partsRaw)
            parts = map(lambda part: (part[0], int(part[1])), parts)
            partRatings.append(dict(parts))
        elif line != "\n":
            workflow = WorkFlow(line)
            workflows[workflow.name] = workflow

    tot = 0
    for part in partRatings:
        workflow = "in"
        while workflow not in ["A", "R"]:
            workflow = workflows[workflow].next(part)
        if workflow == "A":
            tot += sum(part.values())
    pp.pprint(tot)

if __name__ == "__main__":
    main()
