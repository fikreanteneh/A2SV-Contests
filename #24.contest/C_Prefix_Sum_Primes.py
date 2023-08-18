from collections import Counter


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



n = I()
nums = LI()
nums = Counter(nums)
if nums[1] <= 0:
    print( *([2] * nums[2]))
    exit()
if nums[2] <= 0:
    print( *([1] * nums[1]))
    exit()
    
answer = []

if nums[2] > 0:
    answer.append(2)
    answer.append(1)
    nums[2] -= 1
    nums[1] -= 1
answer += [2] * nums[2]
answer += [1] * nums[1]

print(*answer)