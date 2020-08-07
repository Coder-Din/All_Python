'''
import random
n1 = random.randint(1,10)
n2 = random.randint(1,10)
n3 = random.randint(1,10)
while n2 == n1:
    n2 = random.randint(1,10)
while n3 == n1 or n3 == n2:
    n3 = random.randint(1,10)
num = (n1 * 100) + (n2 * 10) + n3
def func(number):
    cows = 0
    bulls = 0
    nnum = str(num)
    nnumber = str(number)
    for j in range(len(nnumber)):
        for i in range(len(nnum)):
            if nnumber[j] == nnum[i] and j == i:
                bulls += 1
            elif nnumber[j] == nnum[i]:
                cows += 1
            else:
                continue
    print(num)
    print(cows, 'cows')
    print(bulls, 'bulls')
func(input('Write a 3 digit number!:'))                
'''
