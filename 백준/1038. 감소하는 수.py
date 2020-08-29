def solution(n):
    if n < 10:
        return n
    if n > 1000000:
        return -1
    res = 9
    result = [str(x) for x in range(0, 11)]
    while res < 1000001:
        tmp = []
        if not result:
            return -1
        for i in range(len(result)):
            num = int(result[i][-1])
            for j in range(num):
                tmp.append(result[i] + str(j))
                res += 1
                if res == n:
                    return tmp[-1]
        result = tmp[:]

    return -1



N = int(input())
print(solution(N))