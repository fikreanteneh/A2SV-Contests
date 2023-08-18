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

for i in range(t):
    stu, n = LI()
    div = LI()
    div.sort()

    total = 2
    count = 0
    
    while div and stu > total:
        total +=(div.pop() - 1)
        count += 1
    if total >= stu:
        print(count)
    else:
        print(-1)