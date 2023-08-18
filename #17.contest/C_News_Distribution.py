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

n, m  = LI()

parent = [i for i in range(n+1)]
rank = [1 for i in range(n+1)]
        

def find(node):
    temp = node
    while node != parent[node]:
        node = parent[node] 
    while temp != parent[temp]:
        temp, parent[temp] = parent[temp], node
    return node

def union(n1, n2):
    p1 = find(n1)
    p2 = find(n2)
    if p1 == p2:
        return
    big, small = (p1, p2) if rank[p1] > rank[p2] else (p2, p1)
    rank[big] += rank[small]
    parent[small] = big


for i in range(m):
    user = LI()
    if user[0] > 1:
        x = user[1]
        for y in range(2, len(user)):
            union(x, user[y])

        
ans = []
for i in range(1, n + 1):
    x = find(i)
    ans.append(rank[x])
print(*ans)      
            
            
