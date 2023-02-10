T = int(input())
 
for tc in range(1,1+T):
    n = int(input())
    words = list(map(str,input().split()))
    median_num = n//2
    result = []
    index = 1
    if n % 2 == 0:
        for q in range(n):
            if q < median_num:
                result.append(words[q])
            else:
                result.insert(index,words[q])
                index += 2
    else:
        for q in range(n):
            if q < median_num+1:
                result.append(words[q])
            else:
                result.insert(index, words[q])
                index += 2
    print('#{}'.format(tc), *result)# 리스트 내부값 호출할때는 .format 쪽이 작성하기 더 편함.