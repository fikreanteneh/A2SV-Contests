from collections import defaultdict


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()

def adjacencyMatrix(matrix):
    graph = defaultdict(lambda: set())
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                graph[i+1].add(j+1)
    return graph

def edgeList(edge):
    graph = defaultdict(lambda: set())
    for i, j in edge:
        graph[i].add(j)
        
        
        
import sys, threading 
from functools import cache


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



    
    
def main(): 
    @cache
    def sol(a, b):
        if b > a:
            return 0
        if a == 0:
            return 1
        answer = 0
        answer += sol(a - 1, b)
        answer += sol(a - 1, b - 1)
        return answer       
    t = I()
    for _ in range(t):
        a, b = LI()
        answer = 2 * sol(a - 1, b - 1)
        answer %= 1000000007
        print(answer)
        
 
 
sys.setrecursionlimit(1 << 30) 
threading.stack_size(1 << 27) 
main_thread = threading.Thread(target = main) 
main_thread.start() 
main_thread.join() 

