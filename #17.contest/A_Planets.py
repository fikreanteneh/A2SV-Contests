from collections import Counter


1`1`


t = I()

for _ in range(t):
    n, c = LI()
    nums = LI()
    nums = Counter(nums)
    answer = 0
    for i, val in nums.items():
        if val >= c:
            answer += c
        else:
            answer += val
    print(answer)