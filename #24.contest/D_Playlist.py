def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



n, k = LI()

bySat = []

byLngth = []

for i in range(n):
    x, y = LI()
    bySat.append((y,x, i))
    byLngth.append((x,y, i))

bySat.sort()
byLngth.sort()

for i in range(n-k):
    
