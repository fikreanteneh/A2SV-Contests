from collections import deque


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



def solution(nums, n):
    last = set([-1])
    que = deque([(0, 0, 0)])
    
    for i, val in enumerate(nums):
        if i - (val + 1) in last:
           last.add(i)
        if i - 1 in last:
            last.add(i + val)
    if n - 1 in last:
        return "YES"
    else:
        return "NO"
    


t = I()
for _ in range(t):
    n = I()
    nums = LI()
    print(solution(nums, n))



