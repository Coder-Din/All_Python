import random
print('You have too guess a random number, less tries, the best')
a = int(input('Guess:'))
r = random.randint(1,100)
coun = 0;

while(a != r):
    if(a >= r):
            print('Random number is smaller')
    else:
        print('Random number is bigger')
    if(coun < 10):
        coun += 1
    else:
        print('Too many tries')
        break
    a = int(input('Try again: '))
if(coun != 10):
    print('Well done!, it took you', coun, 'tries')
else:
    print()

