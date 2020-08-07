'''
imp = input('Write a wise sentence: ')
rep = int(input('Write down how many times the wisdom has to be revealed: '))
for i in range(rep):
    print(imp)

num = int(input())
sen = ''
for i in range(num + 1):
    sen += str(i) + ' '
print(sen)

sen = input('')
for i in range(len(sen)):
    print(sen[i])

product = 1
for i in range(6):
    num = int(input('Write a number'))
    if(num != 0):
        product *= num
    else:
        continue
print(product)

num = int(input('Write a number'))
fcount = 0
factors = ''
for i in range(1, num + 1):
    if(num % i == 0):
        factors += str(i) + ' '
        fcount += 1
    else:
        continue
print(factors)
if(fcount == 2):
    print('Prime')
else:
    print('No')

num = int(input('Write a num'))
cat = False
for i in range(num):
    sen = input('')
    if sen.find('cat') != -1 or sen.find('Cat') != -1:
        cat = True
    else:
        continue
if cat == True:
    print('Maw')

num = int(input('Write a number'))
for j in range(1, num + 1):
    for i in range(1, num + 1):
        print(str(j), '*', str(i), '=', j * i)
'''
a = int(input('Write a number'))
b = int(input('Write a number'))
for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
