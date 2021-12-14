import pprint


numDigits = 10;
numPos = 7;
numTests = 6;

screens = [
    [True, True, True, False, True, True, True],
    [False, False, True, False, False, True, False],
    [True, False, True, True, True, False, True],
    [True, False, True, True, False, True, True],
    [False, True, True, True, False, True, False],
    [True, True, False, True, False, True, True],
    [True, True, False, True, True, True, True],
    [True, False, True, False, False, True, False],
    [True, True, True, True, True, True, True],
    [True, True, True, True, False, True, True]]

easy = [
    [False, False, True, False, False, True, False],
    [True, False, True, False, False, True, False]]
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

# Removes the possibilities of the possible positions of wires
def rem_easy(wires, posses, pos, tester):
    for i in range(numPos):
        if ((tester in wires[pos]) ^ (easy[tester][i])) and i in posses[pos]:
            posses[pos].remove(i)

def main():
    f = open("test.txt")
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
            for j in range(2):
                rem_easy(wires, posses, i, j)
        pp.pprint(posses)

if __name__ == "__main__":
    main()