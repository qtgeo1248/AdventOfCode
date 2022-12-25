import pprint

pp = pprint.PrettyPrinter()
checkNums = 25

def check(nums, n):
    for i in range(len(nums) - checkNums, len(nums)):
        if n - nums[i] in nums[i + 1:]:
            return True
    return False

def findWeakness(nums, target):
    for i in range(len(nums)):
        total = nums[i]
        j = i + 1
        while total < target and j < len(nums):
            total += nums[j]
            j += 1
        if total == target:
            maxNum = None
            minNum = None
            for n in nums[i:j]:
                maxNum = n if maxNum is None or n > maxNum else maxNum
                minNum = n if minNum is None or n < minNum else minNum
            return minNum + maxNum

def main():
    f = open("numbers.txt")

    invalid = None
    nums = []
    while invalid is None:
        n = int(f.readline().rstrip())
        if len(nums) < checkNums:
            nums.append(n)
        elif check(nums, n):
            nums.append(n)
        else:
            invalid = n
    
    print("Answer: " + str(findWeakness(nums, invalid)))
    f.close()

if __name__ ==  "__main__":
    main()