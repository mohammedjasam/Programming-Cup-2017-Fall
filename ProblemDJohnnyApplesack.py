n, k = map(int, input().split())
i = 0


def sub(k):
    # print(n,k)
    global i
    global n
    saved = 0
    while n>0:
        n = n - k
        saved += k - 1
        i+=1
    return(saved)

# print(n)
while i<10:

    print(n)
    n = sub(k)
