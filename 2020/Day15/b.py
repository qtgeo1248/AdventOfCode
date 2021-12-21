import pprint

pp = pprint.PrettyPrinter()
turns = 30000000

def main():
    f = open("numbers.txt")

    nums = f.readline().rstrip().split(",")
    mem = {}
    for t in range(len(nums)):
        mem[int(nums[t])] = t
    last = int(nums[len(nums) - 1])
    for t in range(len(nums), turns):
        speak = 0
        if last in mem.keys():
            speak = t - mem[last] - 1
        mem[last] = t - 1
        last = speak

    print("Answer: " + str(last))
    f.close()

if __name__ ==  "__main__":
    main()