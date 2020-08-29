N, S = map(int, input().split())

numbers = list(map(int, input().split()))

result = len(numbers) + 1

l, r, res, tmp = 0, 0, 0, 0
while 1:
    if S <= res:
        if result > tmp:
            result = tmp
        l += 1
        res -= numbers[l-1]
        tmp -= 1
    elif r >= len(numbers):
        break
    else:
        r += 1
        res += numbers[r-1]
        tmp += 1
if result == len(numbers) + 1:
    result = 0
print(result)


