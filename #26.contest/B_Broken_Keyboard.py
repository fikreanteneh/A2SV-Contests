def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()





t = I()

for _ in range(t):
    a = S()
    answer = set()
    i, j = 0, 0
    n = len(a)
    while i < n:
        while j < n and a[i] == a[j]:
            j += 1
        if (j - i) % 2:
            answer.add(a[i])
        i = j
    
    answer = sorted(list(answer))
    print("".join(answer))