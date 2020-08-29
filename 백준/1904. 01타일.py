N = int(input())
pre1 = 1
pre2 = 2
cur = 0
for i in range(3, N+1):
    cur = pre1 + pre2
    pre1, pre2 = pre2 % 15746, cur % 15746
if N == 1:
    print(pre1)
elif N == 2:
    print(pre2)
else:
    print(cur % 15746)