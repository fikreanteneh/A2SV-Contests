def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()

def sol(n, nums):
    i = 0
    index = []
    while i < n:
        j = i + 1
        while j < n and nums[j] >= nums[j - 1]:
            j += 1
        if j - i > 1:
            index.append((i, j - 1))
        i = j
    answer = index[0][1] - index[0][0] + 1 if index else 1
    for i in range(1, len(index)):
        prevX, prevY = index[i - 1]
        x, y = index[i]
        if prevY + 1 == x:
            if nums[prevY] < nums[x + 1] or nums[prevY - 1] < nums[x]:
                answer = max(answer, y - prevX )
            answer = max(answer, y - prevX )
    return answer
        
     

n = I()
nums = LI()
print(sol(n, nums))