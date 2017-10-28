size = int(input())
array = list(map(int, input().split()))
g = [array[0]]

for x in range(1, len(array)):
    if array[x]>g[-1]:
        g.append(array[x])
    else:
        pass
print(len(g))
g = [str(x) for x in g]
print(" ".join(g))
