
def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()


t=I()
for _ in range(t):
    a,b,c= LI()
    
    d = max(a+b, a+c, b+c, min(a,b)+c, min(b,c)+a, min(a,c)+b, min(a, min(b,c)))
    print(d)