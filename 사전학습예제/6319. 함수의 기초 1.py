def Palindrome(string):
    list_1 = list(string)
    list_2 = list(reversed(list_1))
    count = 0
    for i in range(0, len(list_1)):
        if list_1[i] == list_2[i]:
            count += 1
    if count == len(list_1):
        return True
    else:
        return False

a = input()
if Palindrome(a):
    print(a)
    print('입력하신 단어는 회문(Palindrome)입니다.')

print(reversed(list(a)))