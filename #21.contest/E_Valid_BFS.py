from collections import defaultdict, deque
import sys

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
for _ in range(n - 1):
    u, v = LI()
    graph[u].append(v)
    graph[v].append(u)
possible = LI()


visited = set([1])
que = deque([1])
level = 0
group = []
while que:
    length = len(que)
    group.append(length)
    for l in range(length):
        node = que.popleft()
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                que.append(child)
        graph[node] = level
    level += 1

index = 0
level = 0
for i in group:
    for j in range(index, index + i):
        if graph[possible[j]] != level:
            print("No")
            sys.exit()
    level += 1
    index += i
print("Yes")