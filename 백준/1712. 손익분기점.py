A, B, C = map(int, input().split(' '))
n = A // (C - B) + 1
if B == C or B > C:
    print(-1)
else:
    print(n)

# a + (n*b) < (n*c)
# a < n(c - b)
# a /(c-b) < n (b<c)
# a /(c-b) > n (b>c)
# b != c