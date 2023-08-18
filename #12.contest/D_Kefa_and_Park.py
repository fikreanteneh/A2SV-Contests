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


n, maxi = LI()
nodes = LI()

graph = defaultdict(list)

for i in range(n-1):
    p, c = LI()
    graph[p-1].append(c-1)
    graph[c-1].append(p-1)
ans = 0

stack = [(0, 0)]
visited = set()
while stack:
    # print(stack)
    curr, prev = stack.pop()
    if curr in visited:
        continue
    visited.add(curr)
    prev = prev + 1 if nodes[curr] else 0
    if prev > maxi:
        continue
    if len(graph[curr]) == 1 and curr != 0:
        ans += 1
        continue
    for i in graph[curr]:
        if i != curr:
            stack.append((i, prev))

print(ans)
