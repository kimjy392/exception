import math
def solution(n, k):
    answer = []
    numbers = [x+1 for x in range(n)]
    print(numbers)
    for _ in range(n):
        n = n - 1
        a = k // math.factorial(n)
        b = k % math.factorial(n)
        k = b
        if not b:
            a = a - 1
        answer.append(numbers[a])
        numbers.remove(numbers[a])


    return answer

solution(3, 5)