from math import sqrt
from turtle import right


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

n = I() + 2


num = [1] * (n)
num[0], num[1] = False, False
r = int(sqrt(n)) + 1
for i in range(2, r):
    if num[i] == 1:
        for j in range(i*i, len(num), i):
            num[j] = 2
num = num[2:]
if n >= 5:
    print(2)
else:
    print(1)
print(*num)