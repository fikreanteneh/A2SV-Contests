from heapq import heapify, heappop, heappush


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

def soulution(n, socials):
    social = []
    for i, val in enumerate(socials):
        if val:
            social.append((-1 * val, i + 1))
    heapify(social)

    ans = []
    while len(social) > 1:
        # print(social)
        x = heappop(social)
        y = heappop(social)
        # print(x , "----", y)
        ans.append( sorted([ x[1], y[1] ]))

        x = (x[0] + 1, x[1])
        y = (y[0] + 1, y[1])

        if x[0] != 0:
            heappush(social, x)
        if y[0] != 0:
            heappush(social, y)
        # print(x , "----", y)
        # print("\n")

    print(len(ans))
    # for fr in ans:
    #     print(*fr)



t = I()

for _ in range(t):
    n = I()
    nums = LI()
    soulution(n, nums)