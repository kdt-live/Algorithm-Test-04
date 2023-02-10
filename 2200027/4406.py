T = int(input())

alpha = ['a', 'e', 'i', 'o', 'u']
for _ in range(1,T + 1):
    text = input()
    text = [i for i in text]
    temp = [i for i in text if i not in alpha]
    print(f'#{_} ' + ''.join(temp))