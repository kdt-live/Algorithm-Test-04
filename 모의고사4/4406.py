l= 'aeiou'
tc = int(input())
for j in range(tc):
    s = input()
    for i in l:
        s = s.replace(i,'')
    print(f'#{j+1} {s}')