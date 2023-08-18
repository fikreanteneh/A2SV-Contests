def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



t = I()

for _ in range(t):
    n = I()
    if n == 3:
        print(-1)
        continue
    else:
        arr = []
        flag = False
        if n % 2:
            n -= 1
            flag = True
        for i in range(1, n + 1, 2):
            arr.append(i+1)
            arr.append(i)
        if flag:
            arr.append(n+1)
            arr = arr[n - 2:] + arr[:n - 2]
            arr[0], arr[1] = arr[1], arr[0]
        print(*arr)