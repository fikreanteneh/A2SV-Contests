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

def solution(l, r):
    j = l * 2
    return [l, j]

for _ in range(t):
    l, r = LI()
    if l == r or l == 1:
        print (*[l, r])
    else:
        print(*solution(l,r))
        
        
    