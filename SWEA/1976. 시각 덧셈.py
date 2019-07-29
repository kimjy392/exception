for i in range(int(input())):
    testcase = i + 1
    inpt = list(map(int, input().split()))
    mins = sum(inpt[1::2])
    hour = sum(inpt[0::2])
    if mins >= 60:
        hour += 1
        mins -= 60
    if hour >= 13:
        hour -= 12

    
    print(f'#{testcase} {hour} {mins}')


    
