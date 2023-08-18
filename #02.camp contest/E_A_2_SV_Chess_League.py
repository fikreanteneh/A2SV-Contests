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


n,  maxi = LI()

rating = LI()

new  = deque([])

for i in range(0, 2**n, 2):
    
    p1, p2 = rating[i], rating[i+1]

    if abs(p1 - p2) > maxi:
        wl = (max(p1,p2), max(p1,p2))

    else:
        wl = (max(p1,p2), min(p1,p2))
    new.append(wl)

while(len(new) > 1):
    p1, p2 = new.pop(), new.pop()
    print(p1, p2)

    if p1[1] - p2[0] > maxi:
        new.appendleft(p1)

    elif p2[1] - p1[0] > maxi:
        new.appendleft(p2)
    
    # elif n

    else:
        new.appendleft( (max(p1[0], p2[0]), min(p1[1], p2[1])) )
print(new[0])
answer = []
for i, num in enumerate(rating):
    # print(new[0][0], num, new[0][1], new[0][0] >= num, num >= new[0][1] )
    # print(num >= new[0][0])
    if  new[0][0] >= num and num >= new[0][1]:
        # print("tt")
        answer.append(i+1)

print(*answer)
