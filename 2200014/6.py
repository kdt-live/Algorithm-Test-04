#1 1208

for i in range(10):
    #덤프 횟수
    t=int(input())
    #상자 높이
    arr=list(map(int,input().split()))
    #덤프 횟수만큼
    for j in range(t):
        arr[arr.index(max(arr))]-=1
        arr[arr.index(min(arr))]+=1

        if max(arr)==min(arr):
            break
    print(f'#{i+1} {max(arr)-min(arr)}')


