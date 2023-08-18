from heapq import heapify, heappop


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

num = list(S())
bob = S()

answer = []
zero = []


for val in num:
    if val == "0":
        zero.append(val)
    else:
        answer.append(val)
    
heapify(answer)
ans = []


if answer:
    ans.append(heappop(answer))
if zero:
    ans.extend(zero)
    
while answer:
    ans.append(heappop(answer))
    
ans = "".join(ans)


if ans == bob:
    print("OK")
else:
    print("WRONG_ANSWER")


