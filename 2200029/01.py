# 
import sys
from collections import Counter
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC + 1):
    answer = 'Yes'
    dict = Counter(input())
    for key in dict:
        if len(dict) != 2 or dict[key] != 2:
            answer = 'No'
    print(f'#{tc} {answer}')
        
# 
import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC + 1):
    answer = 'Yes'
    strings = list(input())
    if len(set(strings)) != 2:
        answer = 'No'
    for string in set(strings):
        if strings.count(string) != 2:
            answer = 'No'
    print(f'#{tc} {answer}')