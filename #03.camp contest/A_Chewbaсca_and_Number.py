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


x = I()
x = list(str(x))


new = []
for j, i in enumerate(x):
    if j == 0 and i == "9":
        new.append(i)
    elif int(i) > int(9 - int(i)):
        new.append(str(9-int(i)))
    else:
        new.append(i)

new = "".join(new)

print(int(new))
