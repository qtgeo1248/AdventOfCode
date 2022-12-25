import pprint

pp = pprint.PrettyPrinter()
numBits = 36

def edit(loc, val, xs, mem):
    if len(xs) == 0:
        mem[loc] = val
    else:
        oneBit = 1 << xs[0]
        zeroBit = ((1 << numBits) - 1) ^ oneBit
        edit(loc | oneBit, val, xs[1:], mem)
        edit(loc & zeroBit, val, xs[1:], mem)

def main():
    f = open("program.txt")
    
    # Specifies the bits that are 1's in the mask, so use |
    ones = None
    # Specifies all locations of X's in the mask, using a tuple of indices
    xs = None
    mem = {}

    for line in f:
        if line[1] == 'a': # mask
            mask = line.rstrip().split(" = ")[1]
            ones = 0
            xs = []
            for i in range(len(mask)):
                if mask[i] == '1':
                    ones += 1 << (len(mask) - i - 1)
                elif mask[i] == 'X':
                    xs.append(len(mask) - i - 1)
        elif line[1] == 'e': # mem
            inputs = line.rstrip().split("] = ")
            loc = int(inputs[0].split("[")[1])
            val = int(inputs[1])
            edit(loc | ones, val, tuple(xs), mem)
    ans = 0
    for val in mem.values():
        ans += val

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()