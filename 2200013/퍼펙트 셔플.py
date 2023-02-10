# 퍼펙트 셔플

# 카드를 퍼펙트 셔플 한다는 것은, 카드 덱을 정확히 절반으로 나누고 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 의미한다. 
# 정확한 방식은 다음 그림과 같다.

# N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램을 작성하라.
# 만약 N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 1,000)이 주어진다.
# 두 번째 줄에는 덱에 카드가 놓인 순서대로 N개의 카드 이름이 공백으로 구분되어 주어진다.
# 카드의 이름은 알파벳 대문자와 ‘-’만으로 이루어져 있으며, 길이는 80이하이다.

# [출력]
# 각 테스트 케이스마다 주어진 덱을 퍼펙트 셔플한 결과를 한 줄에 카드 이름을 공백으로 구분하여 출력한다.

# 예제입력
# 3
# 6
# A B C D E F
# 4
# JACK QUEEN KING ACE
# 5
# ALAKIR ALEXSTRASZA DR-BOOM LORD-JARAXXUS AVIANA

# 예제출력
# #1 A D B E C F
# #2 JACK KING QUEEN ACE
# #3 ALAKIR LORD-JARAXXUS ALEXSTRASZA AVIANA DR-BOOM

# 코드

import math
T = int(input()) # 테스트케이스 수 T 입력받기

for i in range(1, T+1): # 테스트케이스 수만큼 실행
    num = int(input()) # 카드 개수 입력받기
    card_deck = list(input().split()) # 카드 종류 리스트로 받기
    result_deck = [] # 빈리스트 형성

    cut = math.ceil(num / 2) # 카드개수를 이등분하고 반올림하여 리스트 슬라이싱 포인트 구하기
    a = card_deck[:cut] # 카드 종류 리스트에서 슬라이싱 포인트로 구분하여 a 리스트, b 리스트로 나누기
    b = card_deck[cut:]

    for j in range(len(a)): # 카드개수가 짝수일 경우, a와 b의 개수가 같지만, 홀수일 경우, a가 1개 더 크기에 a의 길이 만큼 실행
        try:
            result_deck.append(a[j]) # a 리스트의 카드와 b 리스트의 카드를 하나씩 번갈아가며 빈리스트에 추가하기
            result_deck.append(b[j])
        except: # a리스트와 b리스트의 카드개수가 맞지 않아 오류가 생길 경우,
            pass # 패스하기
    
    print(f'#{i}', *result_deck) # 최종적으로 셔플된 리스트 언패킹으로 출력