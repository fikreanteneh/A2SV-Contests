from bisect import bisect_left, bisect_right
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


t = I()

for _ in range(t):
    n, q = LI()
    candy = LI()
    candy.sort(reverse=True)
    runSum = 0
    for i in range(n):
        runSum += candy[i]
        candy[i] = runSum
    # print(candy)
    for x in range(q):
        query = I()
        num = bisect_left(candy, query)
        # print(num, "----------", candy[(num + 1) % n], query)
        if candy[num % n] >= query:
        # if candy[(num + 1) % n] >= query:
            print(num+1)
        else:
            print(-1)
    