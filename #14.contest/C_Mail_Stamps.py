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


n = I()

graph = defaultdict(list)

for _ in range(n):
    x, y = LI()
    graph[x].append(y)
    graph[y].append(x)

for i, j in graph.items():
    if len(j) == 1:
        start = i 
        break

ans = []
stack = [start]
visited = set()
while stack:
    curr = stack.pop()
    ans.append(curr)
    visited.add(curr)
    for ch in graph[curr]:
        if ch not in visited:
            stack.append(ch)

print(*ans)
