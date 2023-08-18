from bisect import bisect_left, bisect_right


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

a,  b = LI()
n =I()
gcds = []
def euclid(x, y):
    if y == 0:
        return x
    return euclid(y, x %y)

x = euclid(b,a)
gcd =[]
for i in range(1, int(x**(0.5))+1):
    if x % i == 0:
        gcd.append(i)
length = len(gcd)
for i in range(length-1, -1, -1):
    y = x//gcd[i]
    if y != gcd[i]:
        gcd.append(x//gcd[i])
# gcd.append(x)
# print(gcd)

for i in range(n):
    low, high = LI()
    index = bisect_right(gcd, high)
    if gcd[index-1] >= low:
        print(gcd[index-1])
    else:
        print(-1)