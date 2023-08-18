import sys


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return list(input())
def I(): return int(input())
def S(): return input()


graph = {"A":[], "B":[], "C":[]}
incoming = {"A":0, "B":0, "C":0}
for _ in range(3):
    a , sign, b = LC()
    if sign == ">":
        graph[a].append(b)
        incoming[b] += 1
    else:
        graph[b].append(a)
        incoming[a] += 1


start = None
for i, j in incoming.items():
    if j == 0:
        start = i
answer = []
if start is None:
    print("Impossible")
    sys.exit()
else:
    que = [start]
    while que:
        node = que.pop()
        answer.append(node)
        
        for i in graph[node]:
            incoming[i] -= 1
            if incoming[i] == 0:
                que.append(i)
        if len(que) > 1:
            print("Impossible")
            sys.exit()
answer.reverse()
print("".join(answer))
        
    

    