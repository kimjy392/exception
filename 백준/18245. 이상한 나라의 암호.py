cnt =0
while 1:
    words = input()
    cnt += 1
    if words == 'Was it a cat I saw?':
        break
    for i in range(0, len(words), 1+cnt):
        print(words[i], end='')
    print()
    