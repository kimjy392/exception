blood = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
dic = {}
for blood_type in blood:
    if blood_type not in dic:
        dic[blood_type] = 1
    else:
        dic[blood_type] += 1
print(dic)