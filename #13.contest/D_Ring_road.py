from collections import defaultdict


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
cost = 0
roads = defaultdict(list)

for _ in range(t):
    l, r, c = LI()
    cost += c
    roads[r].append((l, c))

start = None
for i, j in roads.items():
    if len(j) == 2:
        start = i 
        break
print(roads, start)
x = roads[start][0]
end, ans = x[0], x[1]
print(x)
# print(end, ans)
while end != start and len(roads[end]):
    x = roads[end][0]
    print(x)
    end = x[0]
    ans += x[1]
# print(cost)
print(min(ans, cost - ans))
