def length(words):
    most = ''
    for i in words:
        if len(i) >= len(most):
            most = i
    return most


word = input().split(', ')

print(length(word))