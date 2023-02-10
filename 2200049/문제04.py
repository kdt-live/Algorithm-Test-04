vowel = ['a','e','i','o','u']
for idx in range(int(input())):
  str = input()
  for v in vowel:
    str=str.replace(v,"")
  print(str)