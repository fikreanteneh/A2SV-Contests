import sys, threading
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

def main():
    t = I()
    for _ in range(t):
        ans = 0
        graph = defaultdict(list)
        n = I()
        parent = LI()
        color = S()
        def sol(node):
            mapp = {"B": 0, "W": 1}
            answer = [0, 0]
            answer[mapp[color[node - 1]]] += 1
            for child in graph[node]:
                prev = sol(child)
                answer[0] += prev[0]
                answer[1] += prev[1]
            if answer[0] == answer[1]:
                nonlocal ans
                ans += 1
            return answer

            
            
            
            
        for i, val in enumerate(parent):
            graph[val].append(i + 2)
        sol(1)
        print(ans)
        
   
    
    


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()



# t = I()

# for _ in range(t):
#     n = I()
#     parent = LI()
#     color = S()
#     mapp = {"B": 0, "W": 1}
#     answer = [ [0, 0] for _ in range(n)]
    
#     for i in range(n-2, -1,-1):
#         answer[i + 1] [mapp[color[i + 1]]] += 1
#         answer[parent[i] - 1][0] += answer[i + 1][0]
#         answer[parent[i] - 1][1] += answer[i + 1][1] 
#     # print(answer)
#     ans = 0
#     for i in answer:
#         if i[0] == i[1]:
#             ans += 1
#     print(ans)