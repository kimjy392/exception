N = int(input())

times = list(map(int, input().split()))
times.sort()
result = 0
tmp = 0
for time in times:
    tmp += time
    result += tmp
print(result)