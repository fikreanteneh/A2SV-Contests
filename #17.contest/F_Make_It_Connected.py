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

# answer = 0
minV, minC = mini


costs = [0] * n
for i, val in enumerate(vertices):
    if i != minV:
        costs[i] = (minV, minC + val)
        # answer += (minC + val)
# print(costs)
for _ in range(m):
    x, y, c = LI()
    x -= 1
    y -= 1
    if minV == x or minV == y:
        ind = x if minV == y else y
        if costs[ind][1] < c:
            costs[ind]  = (minV, c)
    else:
        x, y = (x, y) if costs[x][1] < costs[y][1] else (y, x)
        if x-1 != minV and costs[x-1][1] > c:
            decrease = costs[x-1][1]
            increase = c
            costs[x-1] = (y-1, c)
        elif y-1 != minV and costs[y-1][1] > c:
            decrease = costs[y-1][1]
            increase = c
            costs[y-1] = (x-1, c)
ans = 0
for i in costs:
    if i:
        ans += i[1]
print(ans)
    
        