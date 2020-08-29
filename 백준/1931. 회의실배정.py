N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x:(x[1], x[0]))
start = 0
end = 0
result = 0
for i in range(N):
    ts, te = times[i]
    if ts >= end:
        start, end = times[i]
        result += 1
print(result)