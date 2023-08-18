from math import ceil


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



n = I()
m = I()

bench = []
for _ in range(n):
    bench.append(I())

bench.sort()
answer = [0, 0]
answer[1] = bench[-1] + m

extra = 0
for i in range( n -1):
    extra += bench[-1] - bench[i]
if extra >= m:
    answer[0] = bench[-1]
else:
    answer[0] = bench[-1] + ceil((m - extra) / n)
print(*answer)
    

