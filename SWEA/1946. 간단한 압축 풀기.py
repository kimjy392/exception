for i in range(1, int(input())+1):
    testcase = i
    inpt = []
    words = []
    for j in range(int(input())):
        inpt = input().split()
        words.extend(list(inpt[0] * int(inpt[1])))
    
    print(f'#{i}')
    for idx, word in enumerate(words):
        print(word, end='')
        if not (idx+1) % 10 or idx+1 == len(words):
                print()
        