def p1(nums):
    toppointer = len(nums) - 1
    lowpointer = 0

    while(True):
        topvalue = nums[toppointer]
        lowvalue = nums[lowpointer]
        sum = lowvalue + topvalue

        if toppointer is 0:
            print("nomatch")
            break
        elif (sum == 2020):
            print(topvalue*lowvalue)
            break
        elif (sum < 2020):
            lowpointer += 1
        elif (sum > 2020):
            lowpointer = 0
            toppointer -= 1


def p2(nums):
    toppointer = len(nums) - 1
    lowpointer = 1

    while(True):
        topvalue = nums[toppointer]
        lowvalue = nums[lowpointer]
        lowvlowalue = nums[lowpointer-1]
        sum = lowvalue + topvalue + lowvlowalue

        if toppointer is 0:
            print("nomatch")
            break
        elif (sum == 2020):
            print(topvalue*lowvalue*lowvlowalue)
            break
        elif (sum < 2020):
            lowpointer += 1
        elif (sum > 2020):
            lowpointer = 1
            toppointer -= 1



nums = []
with open('inputd1') as f:
    nums = f.readlines()
    nums = [int(i) for i in nums]

nums.sort()

p1(nums)
p2(nums)

