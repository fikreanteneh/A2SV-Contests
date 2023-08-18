def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



def solution(num, n):
    num.sort(reverse=True)
    num[1], num[-1] = num[-1], num[1]
    
    runSum = num[0]
    for i in range(1, n):
        if runSum == num[i]:
            return False
        runSum += num[i]
    return True

# def solution2(num, n):
#     runSum = num[0]
#     for i in range(1, n):
#         if runSum == num[i]:
#             for j in range(i, n):
                
#         runSum += num[i]
#     return True


t = I()

for _ in range(t):
    
    n = I()
    num = LI()
    if n == 2 and num[0] == num[1]:
        print("NO")
    
    elif solution(num, n):    
        print("YES")
        print(*num)
    else:
        print("NO")