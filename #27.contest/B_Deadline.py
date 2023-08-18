from math import ceil


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



def equ(x, d):
    return x + d / (x + 1)

def sol(n, d):
    left, right = 0, d
    while left <= right:
        mid = (left + right) // 2
        curr = equ(mid, d)
        nextt = equ(mid + 1, d)
        if ceil(curr) <= n:
            return "YES"
        if  curr < nextt:
            right = mid - 1
        else:
            left = mid + 1 
    return "NO"
                

t = I()
for _ in range(t):
    n , d = LI()
    print(sol(n, d))