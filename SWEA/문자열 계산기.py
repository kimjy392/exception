# 여기에 코드를 작성하세요.
def calc(words):
    num = ''
    symbol = '+'
    result = 0
    for word in words:
        # word가 +, -이면
        if word in '+-':
            result = result + int(symbol+num)
            # symbol에 저장해라
            symbol = word
            # 지금까지 것을 result에 더하고
            # 지금까지 만든 문자열 초기화
            num = ''
        # word가 숫자면
        else:
            num += word
print(calc('123+2-124'))
print(calc('-12+12-7979+9191'))
print(calc('+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1+1-1'))