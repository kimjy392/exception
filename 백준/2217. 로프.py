N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort()
result = 0
for i in range(N):
    k = N - i
    w = rope[i] * k
    if w > result:
        result = w
print(result)