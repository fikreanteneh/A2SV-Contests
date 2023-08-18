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


t = I()
for _ in range(t):
    n = I()
    nums = LI()
    ans = (1 << 32) - 1
    # print(nums)
    # print(bin(ans))
    for i in nums:
        ans = ans & i 
        # print(i, ans)
    print(ans)

# print(3&1)

