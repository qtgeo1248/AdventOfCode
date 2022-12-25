import pprint

pp = pprint.PrettyPrinter()

CHAR = 0
OR = 1
AND = 2

# Returns [rem] where rem is what is remaining to be matched
def match(msg, rule, rules):
    if rule[0] == CHAR:
        if msg[0:len(rule[1])] == rule[1]:
            return [msg[len(rule[1]):]]
        else:
            return []
    elif rule[0] == OR:
        poss = []
        for r in rule[1]:
            rems = match(msg, r, rules)
            poss.extend(rems)
        return poss
    elif rule[0] == AND:
        poss = [msg]
        for num in rule[1]:
            newPoss = []
            for rem in poss:
                newRems = match(rem, rules[num], rules)
                newPoss.extend(newRems)
            poss = newPoss
        return poss
    else:
        return []

def parse(line, rules):
    line = line.split(" ")
    num = int(line[0].split(":")[0])
    line = line[1:]
    if line[0][0] == '"':
        rules[num] = (CHAR, line[0][1])
    else:
        curNums = []
        rule = []
        sawOr = False
        for tok in line:
            if tok == '|':
                rule.append((AND, tuple(curNums)))
                curNums = []
                sawOr = True
            else:
                curNums.append(int(tok))
        if sawOr:
            rule.append((AND, tuple(curNums)))
            rules[num] = (OR, tuple(rule))
        else:
            rules[num] = (AND, tuple(curNums))

def main():
    f = open("messages.txt")
    
    rules = {}
    isReadingRules = True
    ans = 0
    for line in f:
        if line == '\n':
            isReadingRules = False
            rules[8] = (OR, ((AND, (42,)), (AND, (42, 8))))
            rules[11] = (OR, ((AND, (42, 31)), (AND, (42, 11, 31))))
        elif isReadingRules:
            parse(line.rstrip(), rules)
        else:
            msg = line.rstrip()
            matches = match(line.rstrip(), rules[0], rules)
            foundMatch = False
            for res in matches:
                if len(res) == 0:
                    foundMatch = True
            if foundMatch:
                ans += 1

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()