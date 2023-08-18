def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()


mapp = {"AB", "BA"}



s = S()
def sol(s):
    i = 0
    while i < len(s) - 1:
        if s[i:i+2] in mapp:
            if s[i+1: i + 3] not in mapp:
                mapp.discard(s[i:i+2])
            elif s[i: i + 2] == s[i+2:i+4] :
                i += 1
            i += 2
            while i < len(s) - 1:
                if s[i:i+2] in mapp:
                    return "YES"
                i += 1
        i += 1
        
    return "NO"
                    
        
    
        
print(sol(s))