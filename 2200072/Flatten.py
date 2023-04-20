for test_case in range(1,11):
  flatten_count = int(input())
  box_numbers = sorted(list(map(int, input().split())))

  while flatten_count > 0:
    box_numbers[-1] -= 1
    box_numbers[0]  += 1
    flatten_count -= 1
    box_numbers.sort()
  
  print(f'#{test_case}',box_numbers[-1] - box_numbers[0])
