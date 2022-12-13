import pprint
import functools

pp = pprint.PrettyPrinter()

def getList(line, i): # inp[i] == '['
    curList = []
    i += 1
    while line[i] != ']':
        if line[i] == '[':
            (inner, nextI) = getList(line, i)
            curList.append(inner)
            i = nextI + 1
        if line[i] == ',':
            i += 1
        else:
            nextCom = line.find(',', i)
            nextEnd = line.find(']', i)
            if nextCom != -1 and nextCom < nextEnd:
                curList.append(int(line[i:nextCom]))
                i = nextCom + 1
            elif i != nextEnd:
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

    packets = [[[2]], [[6]]]
    for line in f:
        if line != "\n":
            packets.append(getList(line.strip(), 0)[0])
    packets.sort(key=functools.cmp_to_key(comp))

    tot = 1
    for i in range(len(packets)):
        if packets[i] == [[2]] or packets[i] == [[6]]:
            tot *= i + 1
    print(tot)

if __name__ == "__main__":
    main()
