import datetime
a = input()
b = int(input())
time = 100 - b + int(str(datetime.datetime.now())[:4])
print(f'{a}(은)는 {time}에 100세가 될 것입니다.')