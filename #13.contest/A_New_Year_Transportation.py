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

n, k = LI()
array = LI()

ind = 1 + array[0]
flag = ind == k

while ind != k and ind < n:
    ind = ind + array[ind- 1]
    if ind == k:
        flag = True
        break
if flag:
    print("YES")
else:
    print("NO")    
