def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()


def sol(n, nums):
    for i in nums:
        if i < 0:
            return "NO"
    return "YES"



t = I()

for _ in range(t):
    n = I()
    nums = LI()
    print(sol(n,nums))
    