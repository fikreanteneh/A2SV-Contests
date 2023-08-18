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


n, k = LI()
pair = LI()

index = ( 2 ** n )


pair.sort(reverse=True)

total = 0

while k > 0:
    index //= 2
    total += min(k, index) * pair[index]
    k -= index
print(total)
