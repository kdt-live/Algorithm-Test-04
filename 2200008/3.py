# 모음이 보이지 않는 사람
import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    word = input()
    for chr in 'aeiou':
        word = word.replace(chr, '')
    print(f'#{t} {word}')