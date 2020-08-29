A, B = input().split()
result = 50
for i in range(len(B)-len(A)+1):
    tmp = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            tmp += 1
    result = min(result, tmp)
print(result)