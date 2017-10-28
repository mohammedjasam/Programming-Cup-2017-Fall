limit,  testcases = map(int, input().split())
total = 0
deny = 0
for t in range(testcases):
    s = input().split()
    n = int(s[1])
    # print(s[0],int(s[1]))
    if s[0] == "enter":
        if total + n > limit:
            deny += 1
        else:
            total += n

    elif s[0] == "leave":
        if total - n < 0:
            pass
        else:
            total -= n
print(deny)
