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



t = I()

for t in range(t):

    

    walk, elevator, floor = LI()
    ans = walk * 4
    
    
    for i in range(0,4):
        
        reverse = abs(floor - i) * elevator
        elev = (4 - i) * elevator
        walktime = walk * (i)
        
        # print("reve", reverse, elev, walktime)
        # print("all", reverse + elev + walktime)

        ans = min(ans, (reverse + elev + walktime))
    print(ans)




    
        
