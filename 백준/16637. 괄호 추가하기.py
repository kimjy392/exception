def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def cal(n, lst, isin):
    global result
    if check.get(tuple(lst)):
        return
    if n == t:
        res = int(lst[0])
        if res > result:
            result = res
        return
    check[tuple(lst)] = 1
    for i in range(len(lst)):
        if not isint(lst[i]):
            tmp = 0
            if i > 1 and (isin[i-1] or isin[i + 1]):
                continue
            if lst[i] == '+':
                tmp = int(lst[i-1]) + int(lst[i+1])
            elif lst[i] == '*':
                tmp = int(lst[i-1]) * int(lst[i+1])
            elif lst[i] == '-':
                tmp = int(lst[i-1]) - int(lst[i+1])
            tlst = lst[:i-1] + [str(tmp)] + lst[i+2:]
            tisin = isin[:i-1] + [1] + isin[i+2:]
            cal(n + 1, tlst, tisin)

N = int(input())
number = list(input())
t = N // 2
result = -1e9
check = dict()
isin = [0] * N

cal(0, number, isin)
print(result)