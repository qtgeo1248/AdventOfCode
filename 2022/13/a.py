import pprint

pp = pprint.PrettyPrinter()

def getList(line, i): # inp[i] == '['
    curList = []
    i += 1
    while line[i] != ']':
        if line[i] == '[':
            (inner, nextI) = getList(line, i)
            curList.append(inner)
            i = nextI + 1
        elif line[i] == ',':
            i += 1
        else: # Is integer
            nextCom = line.find(',', i)
            nextEnd = line.find(']', i)
            if nextCom != -1 and nextCom < nextEnd:
                curList.append(int(line[i:nextCom]))
                i = nextCom + 1
            else:
                curList.append(int(line[i:nextEnd]))
                i = nextEnd
    return (curList, i)

def comp(l1, l2):
    if type(l1) == list and type(l2) == list:
        for i in range(len(l1)):
            if i >= len(l2):
                return 1
            check = comp(l1[i], l2[i])
            if check != 0:
                return check
        return 0 if len(l1) == len(l2) else -1
    elif type(l1) == int and type(l2) == int:
        return -1 if l1 < l2 else (0 if l1 == l2 else 1)
    elif type(l1) == int and type(l2) == list:
        return comp([l1], l2)
    else:
        return comp(l1, [l2])

def main():
    f = open("signal.txt")

    first = None
    second = None
    i = 1
    tot = 0
    for line in f:
        if first == None:
            first = line.strip()
        elif second == None:
            second = line.strip()
        else:
            (l1, _) = getList(first, 0)
            (l2, _) = getList(second, 0)
            if comp(l1, l2) < 0:
                tot += i
            i += 1
            first = None
            second = None
    print(tot)

if __name__ == "__main__":
    main()
