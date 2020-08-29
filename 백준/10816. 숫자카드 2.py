N = int(input())
cards = list(map(int, input().split()))
M = int(input())
read = list(map(int, input().split()))
have = [0] * 10000001
mhave = [0] * 10000001
for card in cards:
    if card < 0:
        mhave[-card] += 1
    else:
        have[card] += 1
for card in read:
    if card < 0:
        print('{}'.format(mhave[-card]), end=' ')
    else:
        print('{}'.format(have[card]), end=' ')