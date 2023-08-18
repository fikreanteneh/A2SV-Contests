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


word = S()


capital = 0
small  = 0
n = len(word)
i= n -1
while i >= 0 and word[i].islower():
    i -= 1
# print(i)
ans = 0
for j in range(i, -1, -1):
    if word[j].islower():
        ans += 1

print(ans)    