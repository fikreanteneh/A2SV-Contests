from math import ceil


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
mati = LI()
ibsa = LI()
 
mati.sort()
ibsa.sort()
 
 
count = 0
 
i,  j = 0,0
while i < n and j < n:
    
    while  j < n and ibsa[j] < mati[i]:
        j += 1
    
    if j < n:
        count += 1
        i += 1
        j += 1
    else:
        break
 
count -= (n - i)
added = n - i
print(ceil(added / 2))