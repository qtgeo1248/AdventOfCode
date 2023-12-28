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

def split(rule, partition):

    (l, r) = partition[rule[1]]
    yes = partition.copy()
    no = partition.copy()
    if rule[0]:
        yes[rule[1]] = (l, min(rule[2] - 1, r))
        no[rule[1]] = (max(l, rule[2]), r)
        if rule[2] <= l:
            return (None, no)
        elif l < rule[2] <= r:
            return (yes, no)
        else:
            return (yes, None)
    else:
        yes[rule[1]] = (max(l, rule[2] + 1), r)
        no[rule[1]] = (l, min(rule[2], r))
        if rule[2] < l:
            return (yes, None)
        elif l <= rule[2] < r:
            return (yes, no)
        else:
            return (None, no)

def accepted(name, partitions, workflows):
    if name == "A":
        def totParts(part):
            res = 1
            for val in part.values():
                res *= val[1] - val[0] + 1
            return res
        return sum(map(totParts, partitions))
    if name == "R":
        return 0
    tot = 0
    for rule in workflows[name].rules:
        splits = list(map(lambda partition: split(rule, partition), partitions))
        yeses = [yes for (yes, _) in splits if yes is not None]
        nos = [no for (_, no) in splits if no is not None]
        partitions = nos
        tot += accepted(rule[3], yeses, workflows)
    tot += accepted(workflows[name].end, partitions, workflows)
    return tot

def main():
    f = open("parts.txt")

    workflows = dict()

    for line in f:
        if line != "\n" and line[0] != "{":
            workflow = WorkFlow(line)
            workflows[workflow.name] = workflow

    pp.pprint(accepted("in", [{"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}], workflows))

if __name__ == "__main__":
    main()
