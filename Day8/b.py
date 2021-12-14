import pprint

numPos = 7;

# The ones with only one possible length, so can make definite claims
easy = [
    [False, False, True, False, False, True, False],
    [True, False, True, False, False, True, False],
    [False, True, True, True, False, True, False]]

# If you have a possibility on the left, you can't have a length on the right
hard = {
    1: 3,
    3: 2,
    4: 3,
    5: 3}

'''
My Positions 
   0
  1 2
   3
  4 5
   6
'''

def init(start):
    wires = []
    for _ in range(numPos):
        row = set()
        if start:
            for j in range(numPos):
                row.add(j)
        wires.append(row)
    return wires

# Removes the possibilities of positions of wires with 1, 4, and 7 clues
def rem_easy(wires, posses, pos, tester):
    for i in range(numPos):
        if ((tester in wires[pos]) ^ (easy[tester][i])) and i in posses[pos]:
            posses[pos].remove(i)

# Each thing only has pairs left, so deduces it one by one
def rem_hard(wires, posses):
    for i in range(numPos):
        if len(posses[i]) > 1:
            notRemoved = True
            k = 0
            while notRemoved and k < len(posses[i]):
                tester = list(posses[i])[k]
                if tester in hard.keys() and hard[tester] in wires[i]:
                    notRemoved = False
                    posses[i].remove(tester)
                    other = list(posses[i])[0]
                    for j in range(numPos):
                        if i != j and other in posses[j]:
                            posses[j].remove(other)
                k += 1

def main():
    f = open("test1.txt")
    pp = pprint.PrettyPrinter()
    for line in f:
        wires = init(False)
        code = line.split(" ")
        i = 0
        while code[i] != "|":
            tok = code[i]
            for j in range(len(tok)):
                wires[ord(tok[j]) - ord('a')].add(len(tok) - 2)
            i += 1
        
        posses = init(True)
        for i in range(numPos):
            for j in range(3):
                rem_easy(wires, posses, i, j)
        rem_hard(wires, posses)
        pp.pprint(posses)

if __name__ == "__main__":
    main()