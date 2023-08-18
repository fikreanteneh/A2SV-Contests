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

def solution(n, grid):
    visited=set()
    stack = [(0, 0)]
    while stack:
        x, y = stack.pop()
        visited.add((x,y))
        if x == 1 and y == n - 1:
            return "YES"
        dx = [ (1 - x, y), (x, y + 1), (1 - x, y + 1)]
        for r, c in dx:
            if (r, c) not in visited and grid[r][c] != "1":
                stack.append((r,c))
        # print(stack)
    return "NO"

t = I()
for _ in range(t):
    n = I()
    grid = [list(S()), list(S())]
    grid[0].append("1")
    grid[1].append("1")
    print(solution(n, grid))
