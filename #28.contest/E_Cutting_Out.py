from collections import Counter, defaultdict
from heapq import heapify, heappop, heappush


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()


n, k = LI()

nums = Counter(LI())
nums = list(nums.items())
nums.sort(key = lambda x : x[1])
new =nums[-k:]
ans = []

count = defaultdict(int)
c = 0
i, j = 0, k - 1
while c < k:
    n1, r1 = new[i]
    n2, r2 = new[j]
    if r2 // (count[n2] + 1) > r1 // (count[n1] + 1):
        count[n2] += 1
        i += 1
    elif r2 // (count[n2] + 1) == r1 // (count[n1] + 1):
        count[n2] += 1
        j -= 1 
    else:
        count[n1] += 1
        i += 1
        j -= 1
    c += 1
ans = []
for i, j in count.items():
    ans.extend( [i] * j )
print(*ans)

    
    