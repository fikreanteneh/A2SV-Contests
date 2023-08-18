from collections import deque


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

for _ in range(t):
    n = I()
    insTime = LI()
    duration = LI()
    
    ans = [duration[0] - insTime[0]]
    
    for i in range(1, n):
        if insTime[i] < duration[i-1]:
            ans.append(duration[i] - (duration[i-1]))
        else:
            ans.append(duration[i] - (insTime[i]))
    
    print(*ans) 
    
            
        
        