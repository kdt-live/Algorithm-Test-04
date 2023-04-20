from pprint import pprint
a = int(input())

for i in range(a):
    n,k = map(int,input().split())
    s= []
    for j in range(n):
        b = list(input().split())
        s.append(b)
    pprint(s[0])
    