# def solution(inputString):
#     answer = 0
#     count = {'(': 0, '{' : 0, '[': 0, '<': 0}
#     for char in inputString:
#         if char in '({[<':
#             count[char] += 1
#         elif char in '})]>':
#             if char == ']' and count['[']:
#                 answer += 1
#                 count['['] -= 1
#             elif char == '}' and count['{']:
#                 answer += 1
#                 count['{'] -= 1
#             elif char == ')' and count['(']:
#                 answer += 1
#                 count['('] -= 1
#             elif char == '>' and count['<']:
#                 answer += 1
#                 count['<'] -= 1
#             else:
#                 answer = -1
#                 break
#
#
#     return answer
# print(solution('({(}))'))

def solution(answer_sheet, sheets):
    answer = 0
    for idx, sheet in enumerate(sheets):
        for cidx in range(idx+1, len(sheets)):
            comsheet = sheets[cidx]
            count = 0
            score = 0
            for widx in range(len(sheet)):
                if sheet[widx] == answer_sheet[widx] or comsheet[widx] == answer_sheet[widx]:
                    continue
                else:
                    if sheet[widx] == comsheet[widx]:
                        count += 1
                        tscore = 1
                        if tscore > score:
                            score = tscore
                        for i in range(widx+1, len(sheet)):
                            if sheet[i] == comsheet[i] != answer_sheet[i]:
                                tscore += 1
                            else:
                                if score < tscore:
                                    score = tscore
                                tscore = 0
            tmp = count + (score)**2
            if tmp > answer:
                answer = tmp
    return answer

print(solution(	"4132315142", ["3241523133", "4121314445", "3243523133", "4433325251", "2412313253"]))