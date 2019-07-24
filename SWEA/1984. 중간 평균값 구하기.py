for i in range(int(input())):
   numbers = list(map(int, input().split()))
   del numbers[numbers.index(max(numbers))]
   del numbers[numbers.index(min(numbers))]
   print(f'#{i+1} {round(sum(numbers) / len(numbers))}')