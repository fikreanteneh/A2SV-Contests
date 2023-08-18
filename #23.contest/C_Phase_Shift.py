from collections import deque


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



t = I()

for _ in range(t):
    n = I()
    s = S()
    mapp = {}
    ans = []
    temp = deque(list("abcdefghijklmnopqrstuvwxyz"))
    # index = 0
    # for i in s:
    #     if i in mapp:
    #         ans.append(mapp[i])
    #     else:
    #         while mapp.get(temp[index % 26], "") == i or temp[index % 26] == i:
    #             index += 1
    #         mapp[i] = temp[index % 26]
    #         ans.append(mapp[i])
    #         index += 1
    #     print(mapp, i)
    # print("".join(ans))
        
            
            
    # temp = list("abcdefghijklmnopqrstuvwxyz")
    # index = 0
    for i in s:
        if i in mapp:
            continue
        elif temp[0] == i or mapp.get(temp[0], "")== i:
            temp.append(temp.popleft())
        mapp[i] = temp[0]
        temp.append(temp.popleft())
        print(temp, i)

    for i in s:
        ans.append(mapp[i])
    print("".join(ans))
        
        