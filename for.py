'''
for i in range(1,10):
    print('i * 8 =', i * 8)

for i in [1,4,-8]:
    if i > 0:
        print(i)

num = float(input())
strNum = str(num)
maxDigit = 0
for i in range(len(strNum)):
    if strNum[i] == '.':
        continue
    elif maxDigit < int(strNum[i]):
        maxDigit = int(strNum[i])
print(maxDigit)
'''
string = input('Write a word: ')
sen = ''
for i in range(len(string)-1, 0, -1):
    sen += string[i]
sen += string[0]
if(sen == string):
    print('It is a palindrome')
else:
    print('It is not a palindrome')
    
