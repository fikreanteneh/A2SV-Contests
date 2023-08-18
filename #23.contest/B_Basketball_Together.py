
from math import ceil
 
 
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
 
 
n, enemy = LI()
player = LI()
 
player.sort()
i, j = 0, n-1
ans = 0
while j >= i:
    if player[j] > enemy:
        ans += 1
        j -= 1
        continue
    x  = enemy / player[j]
    i += int(x)
    if i > j:
        break
    ans += 1
    j -= 1

print(ans)