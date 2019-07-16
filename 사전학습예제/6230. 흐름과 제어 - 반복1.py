count = 0
for score in (88, 30, 61, 55, 95):
    count += 1
    if score >= 60:
        print(f'{count}번 학생은 {score}점으로 합격입니다.')
    else:
        print(f'{count}번 학생은 {score}점으로 불합격입니다.')
