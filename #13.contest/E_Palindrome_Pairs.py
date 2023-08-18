from collections import Counter, defaultdict


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
answer = 0
possible = defaultdict(int)

for i in range(n):
    string = Counter(S())
    # remaining = ["0"] * 26
    id = 0
    for letter, count in string.items():
        if count % 2:
            id ^= (1 << (ord(letter) - 97) )
    # remaining.reverse()
    # id = int("".join(remaining), 2)
    answer += possible[id]
    for i in range(26):
        answer += (possible[id ^ (1 << i)])
    possible[id] += 1


print(answer)

