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


def solution(n, tar):
    che = tar.copy()
    count = 0
    i = len(n) - 1
    ans = []
    # print(n, tar)
    while i >= 0 and tar:
        if n[i] != tar[-1]:
            count += 1
        else:
            
            ans.append(tar.pop())
        i -= 1
        # print(tar, i)
    ans.reverse()
    # print(ans, che, count)
    if che == ans:
        return count
    return float("inf")
    
    
    

t = I()

for _ in range(t):
    x = list(str(I()))
    ans = [ solution(x, ["0", "0"]), solution(x, ["2", "5"]), solution(x, ["5", "0"]), solution(x, ["7", "5"]) ]
    print(min(ans))
    


def solution(n, tar):
    che = tar.copy()
    count = 0
    i = len(n) - 1
    ans = []
    # print(n, tar)
    while i >= 0 and tar:
        if n[i] != tar[-1]:
            count += 1
        else:
            
            ans.append(tar.pop())
        i -= 1
        # print(tar, i)
    ans.reverse()
    # print(ans, che, count)
    if che == ans:
        return count
    return float("inf")
    
    
    

t = I()

for _ in range(t):
    x = list(str(I()))
    ans = [ solution(x, ["0", "0"]), solution(x, ["2", "5"]), solution(x, ["5", "0"]), solution(x, ["7", "5"]) ]
    print(min(ans))
    