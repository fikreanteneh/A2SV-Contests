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
 
n, m =LI()
 
graph = defaultdict(list)
nodes = []
for _ in range(m):
    i, j = LI()
    nodes.append((i,j))
    graph[i].append(j)
    graph[j].append(i)
   
def solution(node):
    colour = defaultdict(lambda: -1)
    stack = [(node, 0)]
    
    while stack:
        node, c = stack.pop()
        if colour[node] not in (-1, c):
            return False
        colour[node] = c
        for child in graph[node]:
            if colour[child] != -1:
                if colour[child] != 1 - c:
                    return False
                continue
            stack.append((child, 1 - c))
    return colour
 
start =None
for i in graph:
    start = i
    break
 
x = solution(start)
if x:
    print("YES")
    ans = []
    for i in nodes:
        # print(x)
        if x[i[0]] == 0:
            ans.append("1")
        else:
            ans.append("0")
    print("".join(ans))
else:
    print("NO")