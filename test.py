alph = input()
asc = ord(alph)
print(type(asc))
if len(alph) == 1 and 64<asc and asc<91:
    print('%c(ASCII: %d) => %c(ASCII: %d)'%(asc, asc, asc+32, asc+32))
elif len(alph) ==1 and 96<asc and asc<123:
    print('%c(ASCII: %d) => %c(ASCII: %d)'%(asc, asc, asc-32, asc-32))