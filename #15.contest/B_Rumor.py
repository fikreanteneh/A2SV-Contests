from collections import deque


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

bribe = LI()

nodes = {i:set() for i in range(1, n + 1)}
for _ in range(m):
    i = LI()
    nodes[i[0]].add(i[1])
    nodes[i[1]].add(i[0])

ans = []
visited = set()
for k, v in nodes.items():
    if k in visited:
        continue
    main = set()
    stack = deque([k])
    while stack:
        x = stack.pop()
        if x in visited:
            continue
        main.add(x)
        visited.add(x)
        for i in nodes[x]:
            stack.appendleft(i)
    ans.append(main)

answer = 0
for fri in ans:
    mini = float("inf")
    for g in fri:
        mini = min(mini, bribe[g-1])
    answer += mini
print(answer)