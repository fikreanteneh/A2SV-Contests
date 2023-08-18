def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()


def sol(string):
    i, j = 0, 0
    n = len(string)
    
    while i < n:
        j = i
        while j < n and string[j] == string[i]:
            j += 1
        diff = j - i
        # print(i, j, diff)
        if diff == 1:
            return "NO"
        i = j
    return "YES"
            
    


t = I()
for _ in range(t):
    print(sol(S()))