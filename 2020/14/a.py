import pprint

pp = pprint.PrettyPrinter()
numBits = 36

def main():
    f = open("program.txt")
    
    # Specifies the bits that are 1's in the mask, so use |
    ones = None
    # Specifies the bits that are 0's in the mask, so use &
    zeroes = None
    mem = {}

    for line in f:
        if line[1] == 'a': # mask
            mask = line.rstrip().split(" = ")[1]
            ones = 0
            zeroes = (1 << numBits) - 1
            for i in range(len(mask)):
                if mask[i] == '0':
                    zeroes ^= 1 << (len(mask) - i - 1)
                elif mask[i] == '1':
                    ones += 1 << (len(mask) - i - 1)
        elif line[1] == 'e': # mem
            inputs = line.rstrip().split("] = ")
            loc = int(inputs[0].split("[")[1])
            write = int(inputs[1])
            mem[loc] = (write & zeroes) | ones
    ans = 0
    for write in mem.values():
        ans += write

    print("Answer: " + str(ans))
    f.close()

if __name__ ==  "__main__":
    main()