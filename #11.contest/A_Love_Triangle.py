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


n = I()
nums = LI()

flag = False

for i, val in enumerate(nums):
    num1 = nums[val-1]
    num2 = nums[num1 -1]
    if num2 == i + 1:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO") 