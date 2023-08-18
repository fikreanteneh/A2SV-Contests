from collections import Counter


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()


# t = I()

# for _ in range(t):
#     string = LS()
#     a = Counter(string[0])
#     b = Counter(string[1])
#     answer = 0
#     # print(a, b)
#     for lett, rep in a.items():
#         if lett in b:
#             answer += min(rep, b[lett])
    
#     print(answer)
    
def longest_common_prefix(a, b):
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            return i
    return n

def max_common_prefix(a, b):
    n = len(b)
    prefixes = [longest_common_prefix(a, b)]
    for i in range(n):
        for j in range(i+1, n):
            b_new = list(b)
            b_new[i], b_new[j] = b_new[j], b_new[i]
            prefixes.append(longest_common_prefix(a, "".join(b_new)))
    return max(prefixes)

t = int(input())
for _ in range(t):
    a, b = input().split()
    print(max_common_prefix(a, b))