from collections import defaultdict
import math


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



num = I()


count = defaultdict(int)
while num % 2 == 0:
    count[2] += 1
    num = num // 2
for i in range(3,int(math.sqrt(num))+1,2):
    while num % i== 0:
        count[i] += 1
        num = num / i
if num > 2:
    count[num] += 1
count = list(list(count.items()))
count.sort()

print(count)