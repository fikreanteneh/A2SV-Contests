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


x = LS()
y = LS()

def breakit(arr):
    new = []
    for word in arr:
        if word[0] != "-" or (word[0] == "-" and len(word) == 1):
            new.append(word)
        else:
            new.append(word[0])
            new.append(word[1:])
    return new


def solution(a, b):   
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if x[i] == y[j] and x[i][0] != "-":
            i += 1
            j += 1
            continue
        elif x[i][0] == "-" and y[j][0] == "-":
            i += 1
            j += 1
            return "NO"
        elif x[i][0] == "-" and y[j][0] != "-":
            i += 1
            while j < len(b) and y[j][0] != "-":
                j += 1
            
            j += 1
        elif x[i][0] != "-" and y[j][0] == "-":
            j += 1
            while i < len(a) and x[i][0] != "-":
                i += 1
            
            i += 1
    if i > 
        
a = breakit(x)
b = breakit(y)

print(solution(a, b))

