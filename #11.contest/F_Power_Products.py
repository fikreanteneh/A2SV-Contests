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

n, k = LI()
nums = LI()
special = 0
main = defaultdict(int)
answer = 0
def primeFactors(num):
    global answer
    global special
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
    tot = {}
    needed = {}
    for i, j in count.items():
        j = j % k
        if j:
            tot[i] = j
            needed[i] = k - j
    if not tot:
        answer += special
        special += 1
        return
    
    tot = list(tot.items())
    needed = list(needed.items())
    tot.sort()
    needed.sort()
    tot = tuple(tot)
    needed = tuple(needed)
    answer += main[needed]
    main[tot] += 1

for i in nums:
    primeFactors(i)
print(answer)


