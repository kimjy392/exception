string = input()
num = ''
exp = []
exp = string.split('-')
# for ch in string:
#     if ch == '+' or ch == '-':
#         if num:
#             exp.append(str(int(num)))
#         exp.append(ch)
#         num = ''
#     else:
#         num += ch
# exp.append(str(int(num)))
# m = -1
print(exp)
# for i in range(len(exp)):
#     if exp[i] == '-':
#         m = i
#     elif m != -1 and exp[i] == '+':
#         exp[m + 1] = '(' + exp[m + 1]
#         exp[i + 1] = exp[i + 1] + ')'
# print(eval(''.join(exp)))