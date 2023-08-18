from collections import Counter


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

n, m , k = LI()
soldiers = []
for i in range(m + 1):
    soldiers.append(I())

target = soldiers.pop()
answer = 0

for val in soldiers:
    x = target ^ val
    x = Counter(bin(x))
    if x["1"] <= k:
        answer += 1
print(answer)
