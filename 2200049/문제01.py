for idx in range(10):
  dump = int(input())
  arr = list(map(int,input().split()))
  arr.sort()
  print(arr)
  for _ in range(dump):
    arr[99]-=1
    arr[0]+=1
    arr.sort()
  print(f"#{idx+1}",arr[99]-arr[0])