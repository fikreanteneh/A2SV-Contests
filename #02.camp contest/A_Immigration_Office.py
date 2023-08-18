
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

people = LS()

query = I()


# tobe = []
for i in range(query):
    name =  S()
    left, right = 0, n-1
    while left <= right: 
        mid = left + ((right - left) // 2) 
        if people[mid] < name:
            if mid == n-1:
                print(n)
                break
            elif people[mid + 1] > name:
                print(mid + 1)
                break
            left = mid + 1
        elif people[mid] > name:
            if mid == 0:
                print(0)
                break 
            right = mid - 1  









