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


t = I()

for _ in range(t):
    n, m = LI()
    nums = LI()
    # nums.sort()
    heapify(nums)

    change = LI()
    # change.sort()
    j = 0
    i = 0
    while i < m:
        heappop(nums)
        heappush(nums, change[i])
        # nums[j] = change[i]
        # j += 1 
        i += 1    
    print(sum(nums))