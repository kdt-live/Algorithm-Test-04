TC = int(input())
for _ in range(TC):
    S = input()
    alphabet = S[0]; another_alphabet = []; answer = ""
    S = S.replace(alphabet, "*")
    for i in range(4):
        if S[i] == "*": pass
        else: another_alphabet.append(S[i])
    if len(another_alphabet) == 2 and another_alphabet[0] == another_alphabet[1]:
        answer = "Yes"
    else: answer = "No"
    print("#{} {}".format(_+1, answer))