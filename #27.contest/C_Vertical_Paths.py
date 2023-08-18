from collections import defaultdict


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



def parentFinder(root, graph):
    ans = set([root])
    for i, child in graph.items():
        ans.update(child[1:])
    return list(ans)
        
    # stack = [root]
    # parent = []
    # while stack:
    #     curr = stack.pop()
    #     parent.append(curr)
    #     # print(curr, graph[curr])
    #     for i in range(len(graph[curr])):
    #         stack.append(graph[curr][i])
    # return parent
    

def sol(parent, graph):
    while parent:
        curr = parent.pop()
        temp = [curr]
        while graph[curr]:
            curr = graph[curr][0]
            temp.append(curr)
        print(len(temp))
        print(*temp)
        
            
def graphing(n, par):
    graph = defaultdict(list)
    root = None
    for i in range(n):
        if i + 1 == par[i]:
           root = i + 1
           continue 
        graph[par[i]].append(i + 1)
    return (root, graph) 
    


t = I()
for _ in range(t):
    n = I()
    par = LI()
    root, graph = graphing(n, par)
    parents = parentFinder(root, graph)
    print(len(parents))
    sol(parents, graph)
    if _ != t - 1:
        print()