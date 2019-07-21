def countdown(num):
    if num == 0:
        print('카운트다운을 하려면 0보다 큰 입력이 필요합니다.')
    else:
        while num >= 1:
            print(num)
            num -= 1
countdown(0)
countdown(10)