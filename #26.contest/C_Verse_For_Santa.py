def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



t = I()

for _ in range(t):
    n, s = LI()
    num = LI()
    i, j = 0, 0
    runSum = 0
    maxi = [float("-inf"), -1]
    while i < n and runSum < s:
        runSum += num[i]
        if maxi[0] < num[i]:
            maxi = [num[i], i]
        i += 1
    if  i == n and runSum <= s:
        print(0)
        continue
    else:
        print(maxi[1] + 1)
    