T = int(input())

for t in range (1, T+1) :
    S = input()
    SS = S.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
    print(f"#{t} {SS}")