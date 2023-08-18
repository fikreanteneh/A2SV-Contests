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


def solution(n, tar, nums):
    answer = (( (tar + 1)) * (tar)) // 2
    for i, val in enumerate(nums):
        if val <= tar:
            answer -=(2 * val)
    return int(answer)


t = I()

for _ in range(t):
    n, x = LI()
    nums =LI()
    print( solution(n, x, nums))