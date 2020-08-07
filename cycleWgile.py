'''
while input('Is the monster scary?') != 'Yes':
    print('There is a monster infront of you')
print('So run!')
'''
from random import randint as rn
print('Haunted house')
score = 0

while True:
    ghost_door = rn(1,3)
    print('You are in a big and scary house...')
    print('There are 3 doors infront of you...')
    print('There is a ghost beyond one of them')
    print('Which door will you dare enter to?')
    door_num = int(input('1, 2 or 3?'))
    if(door_num == ghost_door):
        print('Got you! Ghost is right infront of you!')
        break
    else:
        print('You got lucky this time!')
        print('Lets go further...')
        score += 1
print('Run away!')
print(score)
