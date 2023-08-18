def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()

n, t = LI()

nums = [0] + LI()

runSum = 0
for i, num in enumerate(nums):
    runSum += num
    nums[i] = runSum

i = 0
ans = 0
for j in range(1, n + 1):
    while nums[j] - nums[i] > t:
        i += 1
    # print(nums[j] - nums[i])
    # print(i,j)
    ans = max(ans, j - i )
    # print(ans)
    # print()
print(ans)    