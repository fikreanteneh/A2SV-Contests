

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


def solution(n, t, time, ent):
    answer = [-2,-1]
    for i in range(n):
        totalTime = i + time[i]
        sats = ent[i]
        if totalTime <= t and answer[1] < sats:
            answer = [i, sats ]
    return answer[0] + 1



t = I()
for _ in range(t):
    n, t = LI()
    times = LI()
    sat = LI()
    print(solution(n, t, times, sat))