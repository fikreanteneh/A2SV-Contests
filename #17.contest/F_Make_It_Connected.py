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



n, m = LI()
vertices = LI()

mini = (0, vertices[0])
for i, val in enumerate(vertices):
    if val < mini[1]:
        mini = (i, val)

answer = 0
minV, minC = mini


costs = [0] * n
for i, val in enumerate(vertices):
    if i != minV:
        costs[i] = (minV, minC + val)
        answer += (minC + val)
# print(costs)
for _ in range(m):
    x, y, c = LI()
    if x-1 != minV and costs[x-1][1] > c:
        decrease = costs[x-1][1]
        increase = c
        answer -= decrease
        answer += increase
        costs[x-1] = (y-1, c)
    elif y-1 != minV and costs[y-1][1] > c:
        decrease = costs[y-1][1]
        increase = c
        answer -= decrease
        answer += increase
        costs[y-1] = (x-1, c)
ans = 0
for i in costs:
    if i:
        ans += i[1]
print(ans)
    
        