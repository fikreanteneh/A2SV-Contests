



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
    store = defaultdict(int)
    for i, val in enumerate(nums):
        if i % 2 != val % 2:
            store[i%2] += 1
    
    if store[0] != store[1]:
        print(-1)
    else:
        print(store[0])
            