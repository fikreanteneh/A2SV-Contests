from collections import defaultdict


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()


def sol(n, nums):
    if n % 2:
        return "NO"
    count = {}
    pair = defaultdict(set)
    for a, b in nums:
        if a == b:
            return "NO"
        count[a] = count.get(a, 0) + 1
        count[b] = count.get(b, 0) + 1
        pair[a].add(b)
        pair[b].add(a)
    for num in range(1, n + 1):
        if count.get(num, 0) != 2:
            return "NO"
        
    for num in range(1, n//2 + 1):
        
    
    store = set()
    other = set()

    for a, b in nums:
        if a not in store and b not in store:
            store.add(a)
            store.add(b)
        elif a not in other and b not in other:
            other.add(a)
            other.add(b)
        else:
            return "NO"
    if len(store) == n and len(other) == n:
        return "YES"
    return "NO"       
    

t = I()
for _ in range(t):
    n = I()
    nums = []
    for i in range(n):
        x = LI()
        nums.append(tuple(x))
    print(sol(n, nums))