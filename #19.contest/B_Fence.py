def LI():
    return list(map(int, input().split(" ")))
def LS():
    return input().split(" ")
def LC():
    return input().split()
def I():
    return int(input())
def S():
    return input()

n, k = LI()
nums = LI()


runningSum = 0
for i in range(n):
    runningSum += nums[i]
    nums[i] = runningSum

mini = (nums[k - 1], 1)
for i in range(k, n):
    # print(i - k, i, nums[i] - nums[i - k])
    if nums[i] - nums[i - k] < mini[0]:
        mini = (nums[i] - nums[i - k], i - k + 2)
# print(nums)
print(mini[1])
