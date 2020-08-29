K, N = map(int, input().split())
lengths = []
for _ in range(K):
    lengths.append(int(input()))
start = 1
end = max(lengths)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for length in lengths:
        cnt += (length // mid)
    if cnt < N:
        end = mid - 1
    elif cnt >= N:
        start = mid + 1


print(end)