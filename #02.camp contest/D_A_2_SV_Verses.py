from collections import defaultdict


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


n, a, b = LI() 

pro = LI()

left, right = 0, 0

ans = 0
total = 0

def subarry(arr, k):
    left = ans = sums  = 0
    for right in range(len(arr)):
        sums += arr[right]
        while left <= right and sums > k:
            sums -= arr[left]
            left += 1
        ans += (right - left + 1)
    return ans

print(subarry(pro, b) - subarry(pro, a-1))