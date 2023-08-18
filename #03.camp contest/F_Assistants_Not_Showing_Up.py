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




def merge(intervals):
        intervals.sort()
        new = []
        new.append(intervals[0])
        for i in range(1, len(intervals)):
            point1 = new[-1]
            point2 = intervals[i]

            if point2[0] > point1[1]:
                new.append(point2)
            else:
                if point1[1] < point2[1]: point1[1] = point2[1]
        return new

n, m = LI()
answer = []
for i in range(m):
    answer.append(LI())
answer.sort()
# y = merge(answer)
flag = "NO"
first = 1
# print(y)
if answer[0][0] > 0:
    flag = "YES"
if answer[-1][1] < n - 1:
    flag = "YES"

for i in range(1, len(answer)):
    if answer[i][0] - 1 > answer[i-1][1]:
        flag = "YES"
        break
print(flag)