
from collections import Counter


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()


def solution(string):
    total = Counter(string)
    curr = {"0": 0, "1": 0}
    answer = float("inf")
    for i in string:
        curr[i] += 1
        right0 = total["0"] - curr["0"]
        left0 = curr["0"]
        right1 = total["1"] - curr["1"]
        left1 = curr["1"]
        ans1 = left0 + right1 
        ans2 = left1 + right0
        
        answer = min(answer, ans1, ans2)
    return answer
    

t = I()
for _ in range(t):
    string = S()
    print(solution(string))

    
    