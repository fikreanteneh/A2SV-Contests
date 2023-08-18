

from collections import Counter


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



n = I()
nums = LI()
nums.sort()
numss = Counter(nums)
answer = 0
for val in reversed(nums):
    a = numss[val - 1]
    b = numss[val+1]
    