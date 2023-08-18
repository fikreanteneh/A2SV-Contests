from collections import Counter


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


t = I()

for _ in range(t):
    n, c = LI()
    nums = LI()
    nums = Counter(nums)
    answer = 0
    for i, val in nums.items():
        if val >= c:
            answer += c
        else:
            answer += val
    print(answer)