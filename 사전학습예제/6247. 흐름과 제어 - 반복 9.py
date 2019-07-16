stars = "*"*7
i = 1
while i < 5:
    print(f'{stars:^7}')
    stars = stars.replace('*',' ', 2)
    i += 1
    
