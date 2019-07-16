scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
result = 0
score = 0
while len(scores):
    score = scores.pop()
    if score >= 80:
        result += score
print(result)