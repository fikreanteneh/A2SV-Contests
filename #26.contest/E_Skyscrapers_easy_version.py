def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



def sol(n, nums):
    if n == 1:
        return nums
    inc = nums[1] > nums[0]
    i = 1
    while i < n and (nums[i] > nums[i - 1] == inc):
        i += 1
    if i == n:
        return nums
    
        
    
    
    
n  = I()
nums = LI()
print(*sol(n, nums))