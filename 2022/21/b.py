import pprint

pp = pprint.PrettyPrinter()

def doOp(op, vals):
    if op == "+":
        return vals[0] + vals[1]
    elif op == "-":
        return vals[0] - vals[1]
    elif op == "*":
        return vals[0] * vals[1]
    else:
        return vals[0] // vals[1]

def inv(op, need, left, right):
    if left is None:
        if op == "+":
            return need - right
        elif op == "-":
            return need + right
        elif op == "*":
            return need // right
        else:
            return need * right
    else: # right is None
        if op == "+":
            return need - left
        elif op == "-":
            return left - need
        elif op == "*":
            return need // left
        else:
            return left // need

def findVal(m, monkeys, ops, human, need):
    if m == "humn":
        return need
    elif len(monkeys[m]) == 0:
        return ops[m]
    elif m == "root":
        toComp = 0 if human[m] else 1
        toInv = 1 if human[m] else 0
        return findVal(monkeys[m][toInv], monkeys, ops, human, findVal(monkeys[m][toComp], monkeys, ops, human, None))
    elif len(monkeys) == 0:
        return ops[m]
    if human[m] is None:
        vals = [findVal(n, monkeys, ops, human, None) for n in monkeys[m]]
        monkeys[m] = []
        ops[m] = doOp(ops[m], vals)
        return ops[m]
    elif human[m]: # Human is on Right
        left = findVal(monkeys[m][0], monkeys, ops, human, None)
        return findVal(monkeys[m][1], monkeys, ops, human, inv(ops[m], need, left, None))
    else:
        right = findVal(monkeys[m][1], monkeys, ops, human, None)
        return findVal(monkeys[m][0], monkeys, ops, human, inv(ops[m], need, None, right))

def findHum(m, monkeys, human):
    human[m] = None
    if m == "humn":
        return True
    if len(monkeys[m]) == 0:
        return False
    
    left = findHum(monkeys[m][0], monkeys, human)
    right = findHum(monkeys[m][1], monkeys, human)
    if left:
        human[m] = False # False is Left, True is Right, None is nowhere
    elif right:
        human[m] = True
    return left or right

def main():
    f = open("monkeys.txt")

    monkeys = dict()
    ops = dict()

    for line in f:
        line = line.strip().split(": ")
        plus = line[1].split(" + ")
        minus = line[1].split(" - ")
        times = line[1].split(" * ")
        divi = line[1].split(" / ")
        if len(plus) > 1:
            monkeys[line[0]] = plus
            ops[line[0]] = "+"
        elif len(minus) > 1:
            monkeys[line[0]] = minus
            ops[line[0]] = "-"
        elif len(times) > 1:
            monkeys[line[0]] = times
            ops[line[0]] = "*"
        elif len(divi) > 1:
            monkeys[line[0]] = divi
            ops[line[0]] = "/"
        else:
            monkeys[line[0]] = []
            ops[line[0]] = int(line[1])

    human = dict()
    findHum("root", monkeys, human)
    print(findVal("root", monkeys, ops, human, None))

if __name__ == "__main__":
    main()
