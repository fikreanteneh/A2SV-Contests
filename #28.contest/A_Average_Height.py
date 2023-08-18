def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



t = I()

for _ in range(t):
    n =I()
    num = LI()
    listt = [[], []]
    for i in num:
        listt[i%2].append(i)
    listt[1].extend(listt[0])
    print(*listt[1])