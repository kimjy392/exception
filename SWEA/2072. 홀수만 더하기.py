testcase = int(input())
for i in range(1, testcase+1):
    result = 0
    numbers = input()
    numbers = numbers.split(' ')
    print(numbers)
    for num in map(int, numbers):
        if num % 2:
            result += num
    print('#{} {}'.format(i,result))