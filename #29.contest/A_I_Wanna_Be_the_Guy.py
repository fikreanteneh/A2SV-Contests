def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



n = I()
x = set(LI()[1:])
y = set(LI()[1:])
x.update(y)

def sol(n, levels):
    for i in range(1, n + 1):
        if i not in levels:
            return "Oh, my keyboard!"
    return "I become the guy."

print(sol(n, x))
        
    