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


n = I()
graph = defaultdict(list)
for i in range(n):
    graph[I()].append(i+1)

maxi = [0]
def solution(node, num):
    maxi[0] = max(num, maxi[0])
    for i in graph[node]:
        solution(i, num + 1)


solution(-1, 0)
print(maxi[0])