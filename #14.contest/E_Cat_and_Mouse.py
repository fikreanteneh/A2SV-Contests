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
 
def solution(grid, row, col, p, move ):
    for i in range(1, row):
        for j in range(1, col):
            if grid[i][j] == "M":
                mouse = [i, j]
                break
    store = {1: [-1, 0], 2: [1, 0], 3: [0, -1], 4: [0, 1], 0: [0, 0]}
    starts = set()
    total = set()
    last = mouse
    for m in move:
        next = store[m]
        last[0] += next[0]
        last[1] += next[1]
 
    visited = set([tuple(last)])
    fringe = deque([(tuple(last) ,0)])
    while fringe:
        node, level = fringe.pop()
        total.add(node)
        if level >= p:
            continue
        dx = [(node[0] + 1, node[1]), (node[0] - 1, node[1]), (node[0], node[1] + 1), (node[0], node[1] - 1)]
        for d in dx:
            x, y = d
            if d not in visited and grid[x][y] != "#":
                visited.add(d)
                fringe.appendleft((d, level + 1))
    return len(total)
        
 
row, col, p = LI()
grid = [["#"] * (col + 2)]
for _ in range(row):
    grid.append(["#"] + list(S()) + ["#"])
grid.append(["#"] * (col + 2))
move = LI()
print(solution(grid, row + 2, col + 2, p, move))