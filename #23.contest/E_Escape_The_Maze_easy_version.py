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

def solution(graph, friends):
    if 1 in friends:
        return "NO"
    graph[1].append("A")
    visited = set(["A"])
    visited.update(friends)
    vladVisited = set(["A", 1])
    
    vlad = set([1])
    
    while vlad:
        new = set()
        for ch in friends:
            for child in graph[ch]:
                if child not in visited:
                    visited.add(child)
                    new.add(child)
        friends = new
        newVlad = set()
        for ch in vlad:
            for child in graph[ch]:
                if child not in visited and child not in vladVisited and child not in friends:
                    if len(graph[child]) == 1:
                        return "YES"
                    vladVisited.add(child)
                    newVlad.add(child)
        vlad = newVlad
    return "NO"
    


t = I()

for _ in range(t):
    _ = input()
    graph = defaultdict(list)
    n, k = LI()
    friends = set(LI())
    for i in range(n - 1):
        a, b = LI()
        graph[a].append(b)
        graph[b].append(a)
    print(solution(graph, friends))
        
        