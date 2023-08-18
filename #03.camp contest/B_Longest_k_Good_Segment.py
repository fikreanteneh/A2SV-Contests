from collections import defaultdict


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


def atmost(nums, k):
    count = defaultdict(int)
    n = len(nums)
    maxi = [0, 0, 0]
    left  = 0
    for right in range(n):
        count[nums[right]] += 1
        if len(count) > k:
            while left <= right and len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                left += 1
        # print(maxi[-1])
        if right - left + 1 > maxi[-1]:
            maxi[0] = left
            maxi[1] = right
            maxi[2] = right - left + 1
    print(maxi[0] + 1, maxi[1] + 1)

atmost(nums, k)