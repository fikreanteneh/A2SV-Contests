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
for i in range(t):
    n = I()
    weight = LI()
    sums = 0
    for i in range(n):
        sums += weight[i]
        weight[i] = sums
    mini = weight[min(11, n-1)]
    for i in range(11, n, 6):
        mini = min(mini, sums - weight[i])
    print(mini)