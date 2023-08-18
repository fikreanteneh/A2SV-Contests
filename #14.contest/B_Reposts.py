# https://codeforces.com/problemset/problem/522/A
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
graph = {"polycarp": 1}
for i in range(n):
    x = S().split(" ")
    graph[x[0].lower()] = graph[x[2].lower()] + 1
print(max(graph.values())) 