for i in range(int(input())):
    c = input()
    scores =list(map(int, input().split()))
    trash = []
    best = [0, 0]
    for score in scores:
        if score not in set(trash):
            trash.append(score)
            if best[1] < scores.count(score):
                    best[0] = score
                    best[1] = scores.count(score)
            elif best[1] == scores.count(score):
                best[0] = score if best[0] < score else best[0]
    print(f'#{i+1} {best[0]}')

