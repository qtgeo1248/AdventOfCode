import pprint

pp = pprint.PrettyPrinter()

def dfs(m, monkeys, ops, visited):
    if m in visited or len(monkeys[m]) == 0:
        visited.add(m)
        return ops[m]
    vals = [dfs(n, monkeys, ops, visited) for n in monkeys[m]]
    ans = None
    visited.add(m)
    if ops[m] == "+":
        ans = vals[0] + vals[1]
    elif ops[m] == "-":
        ans = vals[0] - vals[1]
    elif ops[m] == "*":
        ans = vals[0] * vals[1]
    else:
        ans = vals[0] // vals[1]
    ops[m] = ans
    return ans

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

    visited = set()
    print(dfs("root", monkeys, ops, visited))

if __name__ == "__main__":
    main()
