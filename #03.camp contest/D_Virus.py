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



test = I()
for t in range(test):
    n, infect = LI()
    infected = LI()
    infected.append(infected[0])
    for i in range(infect-1):
        infected[i] = infected[i + 1] - infected[i] - 1
    infected[infect-1] = ( n - infected[infect-1] + infected.pop() - 1)
    infected.sort(reverse = True)
    print(infected)
    protected = 0
    for i in range(infect):
        if
        x = (infected[i] - 1) + (-4 * i)
        # print("---", x)
        if x >= 0:
            protected += (x)
    print(n - protected)



