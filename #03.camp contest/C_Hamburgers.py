from collections import Counter


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


recipe = S()
present = LI()
price = LI()
rubles = I()

recipe = Counter(recipe)
present = {"B":present[0], "S": present[1], "C": present[2]}
price = {"B":price[0], "S": price[1], "C": price[2]}

ans = min (present["B"] // recipe["B"], present["S"] // recipe["S"], present["C"] // recipe["C"])


for i in present:
    present[i] -= (ans * recipe[i])
while sum(present.values()) > 0:
    needed = 0
    for i in present:
        x = price[i] if recipe[i] - present[i] > 0
        needed += 
        present[i] = present[i] - recipe[i] if present[i] > recipe[i] 

recipeNeed = 

for i in  

recipeNeeded = [present[0]]
