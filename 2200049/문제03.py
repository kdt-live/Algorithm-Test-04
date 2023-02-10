import math
from collections import deque
for idx in range(int(input())):
  N = int(input())
  arr = list(input().split())
  a = deque(list(arr[0:math.ceil(len(arr)/2)]))
  b = deque(list(arr[math.ceil(len(arr)/2):len(arr)]))
  print(a)
  print(b)
  ans = []
  while a or b:
    if a:
      ans.append(a.popleft())
    if b:
      ans.append(b.popleft())
  print(f"#{idx+1}",*ans)