from collections import defaultdict, deque


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



def solution(graph):
    que = deque([])
    for node, child in graph.items():
        if len(child) == 1:
            que.append((node, 1))
    ans = []
    while que:
        length = len(que)
        # print(que)
        ans.append(length)
        for _ in range(length):
            curr, level = que.pop()
            for child in graph[curr]:
                graph[child].discard(curr)
                if len(graph[child]) == 1:
                    que.appendleft((child, level + 1))
            graph.pop(curr)
    # print(ans)
    x, y = ans[1], ans[0]//ans[1]
    print(x, y)



t = I()

for _ in range(t):
    graph = defaultdict(set)
    vertices, edge = LI()
    for i in range(edge):
        a, b = LI()
        graph[a].add(b)
        graph[b].add(a)
    solution(graph)
    
    