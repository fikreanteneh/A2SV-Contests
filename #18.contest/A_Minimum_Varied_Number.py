def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I():return int(input())
def S(): return input()


def solution(n, i = 9, prev = set()):
    if n < 10 and n not in prev:
        return str(n)
    if n <= 0:
        return ""
    prev.add(i)
    
    return solution(n - i, i - 1, prev) + str(i)
    

t = I()

for _ in range(t):
    x = I()
    prec = set()
    print(solution(x, 9, prec))
    