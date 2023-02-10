T = int(input())
for t in range(1, T+1):
    a = int(input())
    card = list(input().split())
    d = len(card)//2
    card1 = []
    card2 = []
    if len(card)%2 == 1: # 홀수 일떄 앞부분 3 뒷부분 2이므로 +1
        for i in range(d+1):
            card1.append(card[i]) # 앞부분 저장
        else:
            for j in range(d): 
                card2.append(card[j+d+1]) # 뒷부분 저장 앞부분이 한장을 더 가져감으로 +1
    else:
        if len(card)%2 == 0: # 짝수 일때
            for k in range(d):
                card1.append(card[k]) # 앞부분
            else:
                for l in range(d):
                    card2.append(card[l+d]) # 뒷부분
    suffle = []
    if len(card)%2 == 0: # 짝수
        for q in range(d):
            suffle.append(card1[q]) # 앞장 순서대로
            suffle.append(card2[q]) # 뒷장 순서대로
    else:
        if len(card)%2 == 1: # 홀수
            for w in range(d):
                suffle.append(card1[w]) # 앞장 순서대로
                suffle.append(card2[w]) # 뒷장 순서대로
            else:
                suffle.append(card1[d]) # 마지막 부분 추가
    print(f'#{t}', *suffle)