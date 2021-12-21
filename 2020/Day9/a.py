import pprint

pp = pprint.PrettyPrinter()
checkNums = 25

def check(nums, n):
    for i in range(len(nums)):
        if n - nums[i] in nums[i + 1:]:
            return True
    return False

def main():
    f = open("numbers.txt")

    invalid = None
    nums = []
    while invalid is None:
        n = int(f.readline().rstrip())
        if len(nums) < checkNums:
            nums.append(n)
        elif check(nums, n):
            nums.pop(0)
            nums.append(n)
        else:
            invalid = n
    
    print("Answer: " + str(invalid))
    f.close()

if __name__ ==  "__main__":
    main()