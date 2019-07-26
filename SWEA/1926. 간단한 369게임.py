num = input()
result = ''
for i in range(1, int(num)+1):
    tmp = str(i)
    while '3' in tmp or '6' in tmp or '9' in tmp:
        if '3' in tmp:
            tmp = tmp.replace('3', '-')
        if '6' in tmp:
            tmp = tmp.replace('6', '-')
        if '9' in tmp:
            tmp = tmp.replace('9', '-')
        if tmp.count('-') < len(tmp):
            tmp = '-'

    if i == int(num):
        result += tmp
    else:
        result += tmp + ' '

print(result)