from heapq import heapify, heappop, heappush

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


n =I()
nums = []
heapify(nums)
ans = []
for _ in range(n):
    # print(ans)
    que = list(LS())
    # print(que)
    if que[0] in ("insert, getMin"):
        que[1]= int(que[1])

    if que[0] == "insert":
        heappush(nums, que[1])
        ans.append( f"insert {que[1]}")

    elif que[0] == "removeMin":
        if not nums:
            ans.append( "insert 0")
            heappush(nums, 0)
        heappop(nums)
        ans.append("removeMin")

    else:
        # print(nums)
        if nums and nums[0] == que[1]:
            ans.append(f"getMin {que[1]}")
        elif not nums or nums[0] > que[1]:
            # print('xxx')
            heappush(nums, que[1])
            ans.append(f"insert {que[1]}" )
            ans.append(f"getMin {que[1]}")
        else:
            while nums and nums[0] < que[1]:
                heappop(nums)
                ans.append("removeMin")
            if nums and nums[0] == que[1]:
                ans.append(f"getMin {que[1]}" )
            else:
                ans.append(f"insert {que[1]}")
                ans.append(f"getMin {que[1]}")
print(len(ans))
# print(ans)
for j in ans:
    print(j)



        