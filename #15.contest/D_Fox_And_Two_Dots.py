

from collections import deque


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


def solution(n, m, grid):
    visited = set()
    que = deque([((1,1), (0,0))])
    while que:
        node, parent = que.pop()
    def sol(node. parent, depth):
        if sol in visited


n, m = LI()
grid = []
grid.append(0, [0] * (m + 2))
for _ in range(n):
    i = list(S())
    i.insert(0,0)
    i.append(0)
    grid.append(i)
grid.append(0, [0] * (m + 2))
print(solution(n, m, grid))
