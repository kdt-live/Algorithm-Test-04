#3 4406

t=int(input())
arr='aeiou'

for i in range(t):
    a=input()
    for j in a:
        if j in arr:
            a=a.replace(j,'')
    print(f'#{i+1} {a}')