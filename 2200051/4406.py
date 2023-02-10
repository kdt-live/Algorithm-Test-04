t=int(input())
for i in range(t):
    str=input()
    str=list(str)
    while 'a' in str:
        str.remove('a')
    while 'e' in str:
        str.remove('e')
    while 'i' in str:
        str.remove('i')
    while 'o' in str:
        str.remove('o')
    while 'u' in str:
        str.remove('u')
    str="".join(str)
    print(f"#{i+1} {str}")
# for i in range(t):
#     print(f"#{i+1} {str}")