alph = input()
asc = ord(alph)
print(type(asc))
if len(alph) == 1 and 64<asc and asc<91:
    print('%c(ASCII: %d) => %c(ASCII: %d)'%(asc, asc, asc+32, asc+32))
elif len(alph) ==1 and 96<asc and asc<123:
    print('%c(ASCII: %d) => %c(ASCII: %d)'%(asc, asc, asc-32, asc-32))
# .format()은 자료형을 지정하지 못한다.
# % 포맷팅은 유니코드나 아스키값을 문자로 바꾸기 위해서는 %c을 써야한다.
# upper()를 쓸수 있는건 비밀