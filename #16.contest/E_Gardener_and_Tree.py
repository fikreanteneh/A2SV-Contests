
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

t = I()
_ = S()

def solution(graph, k):
    if k == 0:
        return graph
    que = deque([])
    for node, child in graph.items():
        if len(child) == 1:
            que.append((node, 1))
    depth = 0
    # print(graph)
    # print(que)
    while que and depth < k:
        length = len(que)
        for _ in range(length):
            curr, level = que.pop()
            for child in graph[curr]:
                graph[child].discard(curr)
                if len(graph[child]) == 1:
                    que.appendleft((child, level + 1))
            graph.pop(curr)
        depth += 1
    return graph
                
                
    

for _ in range(t):
    n, k = LI()
    graph = defaultdict(lambda: set())
    for q in range(n-1):
        i, j  = LI()
        graph[i].add(j)
        graph[j].add(i)
    if _ != t-1:
        s = S()
    
    print(len(solution(graph, k)))