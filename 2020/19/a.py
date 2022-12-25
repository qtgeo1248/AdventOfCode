import pprint

pp = pprint.PrettyPrinter()

CHAR = 0
OR = 1
AND = 2

# Returns (isMatched, rem) where rem is what is remaining to be matched
# If it didn't match, rem is None
def match(msg, rule, rules):
    if rule[0] == CHAR:
        if msg[0:len(rule[1])] == rule[1]:
            return (True, msg[len(rule[1]):])
        else:
            return (False, None)
    elif rule[0] == OR:
        for r in rule[1]:
            (isMatched, rem) = match(msg, r, rules)
            if isMatched:
                return (True, rem)
        return (False, None)
    elif rule[0] == AND:
        for num in rule[1]:
            (isMatched, rem) = match(msg, rules[num], rules)
            if not isMatched:
                return (False, None)
            msg = rem
        return (True, msg)
    else:
        return (False, None)

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
        elif isReadingRules:
            parse(line.rstrip(), rules)
        else:
            (isMatching, res) = match(line.rstrip(), rules[0], rules)
            if isMatching and len(res) == 0:
                ans += 1

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()