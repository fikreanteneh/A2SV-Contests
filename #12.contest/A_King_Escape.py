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



n = I()
q = LI()
k = LI()
c = LI()

posy = (0, q[0])  if q[0] > k[0] else (q[0], n) 
posx = (0, q[1]) if q[1] > k[1] else (q[1], n)

# print(posy, posx)

if  posy[0] <= c[0] <= posy[1] and  posx[0] <= c[1] <= posx[1]:
    print("YES")
else:
    print("NO")