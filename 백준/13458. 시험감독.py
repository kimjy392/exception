N = int(input())

rooms = list(map(int, input().split()))
B, C = map(int, input().split())
result = N
flag = 0
for population in rooms:
    population -= B
    if population <= 0:
        continue
    result += population // C
    if population % C:
        result += 1
print(result)