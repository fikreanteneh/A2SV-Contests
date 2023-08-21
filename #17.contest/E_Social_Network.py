from heapq import heappush


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
parent = [i for i in range(n+1)]
rank = [1 for i in range(n+1)]


def find(node):
    temp = node
    while node != parent[node]:
        node = parent[node]
        
    while temp != parent[temp]:
        x = parent[temp]
        parent[temp] = node
        temp = x
    return node

def union(n1, n2, total):
    p1 = find(n1)
    p2 = find(n2)
    if p1 == p2:
        return True
    if rank[p1] < rank[p2]:
        p1, p2 = p2, p1
    rank[p1] += rank[p2]
    parent[p2] = p1
    heappush(total, rank[p1])
    
def solution(a, b):
    total = []
    union(a, b, total)
    return -1 * total[0]    
for _ in range(m):
    x, y = LI()
    print(solution(x, y))
    


