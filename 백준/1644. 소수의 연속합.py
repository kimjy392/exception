N = int(input())

visit = [0] * (N+1)
numbers = []
visit[1] = 1
for i in range(2, N+1):
    if not visit[i]:
        numbers.append(i)
        for j in range(i, N+1, i):
            visit[j] = 1
l, r, s, result =0, 0, 0, 0

while 1:
    if N < s:
        l += 1
        s -= numbers[l-1]
    elif r >= len(numbers):
        break
    else:
        r += 1
        s += numbers[r-1]
    if N == s:
        result += 1
print(result)