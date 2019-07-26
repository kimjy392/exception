for i in range(int(input())):
    testcase = i + 1
    money = int(input())
    count = [0, 0, 0, 0, 0, 0, 0, 0]
    while money - 50000 >= 0:
        money -= 50000
        count[0] += 1

    while money - 10000 >= 0:
        money -= 10000
        count[1] += 1

    while money - 5000 >= 0:
        money -= 5000
        count[2] += 1

    while money - 1000 >= 0:
        money -= 1000
        count[3] += 1

    while money - 500 >= 0:
        money -= 500
        count[4] += 1

    while money - 100 >= 0:
        money -= 100
        count[5] += 1

    while money - 50 >= 0:
        money -= 50
        count[6] += 1

    while money - 10 >= 0:
        money -= 10
        count[7] += 1

    print(f'#{testcase}')
    print(count[0], count[1], count[2], count[3], count[4], count[5], count[6], count[7])


