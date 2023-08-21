def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()


def sol(n, nums):
    ans = 0
    alice, bob = 0, 0
    left, right = 0, n - 1
    while left <= right:
        if alice > bob:
            bob += nums[right]
            right -= 1
        else:
            alice += nums[left]
            left += 1
        # print(alice, bob)
        if alice == bob:
            ans = (left - 0 + n - 1 - right)
    return ans
                




t = I()
for _ in range(t):
    n = I()
    nums = LI()
    print(sol(n, nums))