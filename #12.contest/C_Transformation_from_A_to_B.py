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


a, b = LI()

stack = []
def solution(num):
    stack.append(num)
    if num == b:
        return True
    
    elif num > b:
        return False
    
    if solution(num * 2):
        return True
    stack.pop()
    if solution( (num*10) + 1):
        return True
    stack.pop()
if solution(a):
    print("YES")
    print(len(stack))
    print(*stack)
else:
    print("NO")