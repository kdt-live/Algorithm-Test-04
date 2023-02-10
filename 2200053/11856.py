import sys
sys.stdin = open('2200053/input.txt')

T =int(input())

for t in range(1, T+1):
    s = list(input())
    #print(s)
    result = 0

    for i in range(4):
        #print(s[i])
        cnt = 0
        for j in range(4):
            #print(s[i], s[j])
            if s[i] == s[j]:
                cnt += 1
            #print(cnt)
        if cnt == 2:
            result += 1
    #print(result)
    if result == 4:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')