for i in range(int(input())):
    testcase = i + 1
    students = list(map(int, input().split()))
    scores = []
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D']

    for stu_num in range(int(students[0])):
        score = list(map(int, input().split()))
        scores.append((score[0]*0.35 + score[1]*0.45 + score[2]*0.20, stu_num+1))
        scores.sort()
        scores.reverse()

    num = students[0] // 10
    for idx, value in enumerate(scores):
        if students[1] in value:
            print(f'#{testcase} {grade[((idx+1) // num ) - 1 ]}')


    















# 1
# 10 2
# 87 59 88
# 99 94 78
# 94 86 86
# 99 100 99
# 69 76 70
# 76 89 96
# 98 95 96
# 74 69 60
# 98 84 67
# 85 84 91