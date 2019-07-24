inpt = ['1', '1', '3', '1', '2']
inpt = list(map(int, inpt))
sa = []
pal = 0
for i in inpt:
    if not sa or inpt[-1] == i:
        sa.append(i)
    elif sa[-1] <= i:
        sa.append(i)
    elif sa[-1] > i or inpt[-1] == i:
        print(sa)
        pal += sa[-1] * len(sa[:-1]) - sum(sa[:-1])
        sa = [i]   

print(pal)