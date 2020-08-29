def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        b1 = list(map(int, format(arr1[i], 'b').zfill(n)))
        b2 = list(map(int, format(arr2[i], 'b').zfill(n)))
        result = ''
        for i in range(n):
            if b1[i] or b2[i]:
                result += '#'
            else:
                result += ' '
        answer.append(result)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))