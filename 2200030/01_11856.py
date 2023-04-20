'''11856. 반반
길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때, S에 정확히 두 개의 서로 다른 문자가 등장하고, 각 문자가 정확히 두 번 등장하는 지 판별하라.

[입력]  첫 번째 줄에 테스트 케이스의 수 TC가 주어진다. 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다. 각 테스트 케이스는 다음과 같이 구성되었다.
    ∙ 첫 번째 줄에 문자열 S가 주어진다.

[출력]  각 테스트 케이스마다
    ∙ 조건이 만족되면 “Yes”, 아니면 “No” 를 출력하라.'''
'''5
ABAB
CCDD
EFFE
EEEE
NONE'''
#1 Yes
#2 Yes
#3 Yes
#4 No
#5 No

import sys
sys.stdin = open("input.txt", "r")

for T in range(1,int(input())+1):
    word = str(input())
    cnt = 0
    for w in word:
        if word.count(w) == 2:
            cnt += 1
    if cnt == 4:
        print(f'#{T} Yes')
    else:
        print(f'#{T} No')