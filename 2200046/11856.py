# 반반

from collections import Counter

t = int(input())

for i in range(t):
    # Counter를 이용해 입력받은 문자열의 문자를 센다.
    s = Counter(input())
    # values() 메서드를 이용해 문자의 개수만 추출한다.
    letter_count = list(s.values())
    
    # 문자의 개수 리스트 순회
    # 0이 아닌 숫자가 나오면 No 출력 후 break
    # for문을 온전히 다 돌고 빠져나온 경우 Yes 출력
    for num in letter_count:
        if num != 2:
            print(f'#{i + 1} No')
            break
    else:
        print(f'#{i + 1} Yes')