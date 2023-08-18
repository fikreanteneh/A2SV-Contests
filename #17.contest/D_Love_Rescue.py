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


parent = [i for i in range(26)]
rank = [0 for i in range(26)]

def parentChild(node):
    stack = []
    while node != parent[node]:
        stack.append(node)
        node = parent[node]
    return (node, stack)
        
def find(node1, node2):
    p1, child1 = parentChild(node1)
    p2, child2 = parentChild(node2)
    if p1 == p2:
        return True
    big, small, bigC, smallC = (p1, p2, child1, child2) if rank[p1] >= rank[p2] else (p2, p1, child2, child1)
    smallC.append(small)
    rank[big] += len(smallC)
    while smallC:
        x = smallC.pop()
        rank[x] = 0
        parent[x] = big
        
n = I()
s1 = S()
s2 = S()
# print(ord('a'))
edges = set()
for i in range(n):
    if s1[i] != s2[i]:
        # print(ord(s1[i]) - 97, ord(s2[i]) - 97)
        find(ord(s1[i]) - 97, ord(s2[i]) - 97)


ans = []
for i in range(26):
    if i != parent[i]:
        ans.append((chr(parent[i] + 97), chr(97 + i)))
print(len(ans))
for i in ans:
    print(i[0], i[1])
    