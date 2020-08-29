N, M = map(int, input().split())

array = list(map(int, input().split()))
l, r, s = 0, 0, 0
result = 0
while 1:
    if M <= s:
        l += 1
        s -= array[l-1]
    elif r >= len(array):
        break
    else:
        r += 1
        s += array[r-1]

    if s == M:
        result += 1
print(result)

