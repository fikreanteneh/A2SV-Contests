def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



n, c = LI()
nums = LI()

answer = 1
for i in range(1, n):
    if nums[i] - nums[i-1] <= c:
        answer += 1
    else:
        answer = 1
print(answer)