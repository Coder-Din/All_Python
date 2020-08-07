'''
n = int(input('num:'))
x = 0
tstr = ''
while x < n:
    x += 1
    stri = str(input('sentence: '))
    tstr += stri
print(tstr)

sentence = input('Sentence: ')
a = 0
isa = ''
b = 0
isb = ''
while (sentence[a] != 'a'):
    if(a < len(sentence)):
        a += 1
    else:
        isa = False
        break
while (sentence[b] != 'b'):
    if(b < len(sentence)):
        b += 1
    else:
        isb = False
        break
if(a > b):
    print('b is first')
elif(a < b):
    print('a is first')
else:
    print('There is no a nor b')

sentence = input('Write something:')
print(sentence.replace('i', 'I'))

sentence = input('Write something:')
print(sentence.replace('a', 'ai'))

string = input()
newString = ""
index = 0
while index < len(string):
    if string[index].isalpha():
        newString += string[index]
    index += 1
print(newString)

string = input() + " " 
maxLen = 0
word = ""
result = ""
index = 0
while index < len(string):
    if not string[index].isspace() :
        word += string[index]          
    else:
        if len(word) > maxLen:
            maxLen = len(word)
            result = word
        word = ""
    index += 1
print(result)

import random
newString = ''
index = 0
while len(newString) < 10:
    if(len(newString)%2 == 0):
        newString += random.choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    else:
        newString += random.choice(['1','2','3','4'])
print(newString)


string = input() 
word = ''
word1 = ''
result = ''
index = 0
while index < len(string):
    if not string[index].isspace() :
        word += string[index]          
    else:
        word1 = word
        word = ''
    index += 1
if(len(word) > len(word1)):
    result += word
    result += ' '
    result += word1
else:
    result += word1
    result += ' '
    result += word
print(result)

string = input('')
ob = string.count('(')
cb = string.count(')')
os = string.count('[')
cs = string.count(']')
oc = string.count('{')
cc = string.count('}')
if(ob == cb and os == cs and oc == cc):
    print('Yes')
else:
    print('No')
'''
string = input('Write') + ' '
sl = ''
fl = ''
word = ''
index = 0
while index < len(string):
    if not string[index].isspace() :
        index += 1
        continue          
    else:
        fl = string[index - 1]
        sl = string[index + 1]
        if(fl == sl):
            index += 1
            continue
        else:
            index += 1
            while index < len(string):
                if not string[index].isspace():
                    word += string[index]
                else:
                    print(word)
                    break
                index += 1
            break
        continue
 

