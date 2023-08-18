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


def solution(n, nums):
    count = {}
    for i,val in enumerate(nums):
        c = 0
        while val % 2 == 0:
            val //=2
            c += 1
        count[i] = c
    total = sum(count.values())
    maxi = float("-inf")
    for i,val in enumerate(nums):
        mul = total - count[i]
        nums[i] <<= mul # (2 ** mul)
        for j in range(n):
            if j != i and  count[j] != 0:
                nums[j] >>= count[j] #// (2 ** count[j])
        
        maxi = max(maxi, sum(nums))
        nums[i] >>= mul#// (2 ** mul)
        for j in range(n):
            if j != i and count[j] != 0:
                nums[j] <<= count[j] # (nums[j] * (2 ** count[j]))
    return maxi






t = I()
for _ in range(t):
    n = I()
    nums = LI()
    print(solution(n, nums))