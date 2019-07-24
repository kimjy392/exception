for s in range(int(input())):
    c =input()
    inpt = list(map(int, input().split()))
    sa = inpt[:]
    pal = 0
    num = max(inpt)
    for j,i in enumerate(inpt):
        if num != i:
            pal += num - i
        elif num == i:
            if i == inpt[-1]:
                num = inpt[-1]
            else:
                del sa[:sa.index(i)+1]
                num = max(sa)
    print(f'#{s+1} {pal}')

    # for s in range(int(input())):
    # c =input()
    # inpt = list(map(int, input().split()))
    # pal = 0
    # num = max(inpt)
    # for j,i in enumerate(inpt):
    #     if num != i:
    #         pal += num - i
    #     elif num == i:
    #         if i == inpt[-1]:
    #             num = inpt[-1]
    #         else:
    #             num = max(inpt[j+1:len(inpt)])
    # print(f'#{s+1} {pal}')