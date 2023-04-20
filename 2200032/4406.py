T = int(input())
for test_case in range(1, T+1):
    string = input().strip()
    vowel = ['a', 'e', 'i', 'o', 'u']
    stack = []
    for i in string:
        if i not in vowel:
            stack.append(i)
    print(f"#{test_case} {''.join(stack)}")