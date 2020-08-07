a = 10
if(a%2 == 0) and (a % 10 == 0):
    print('2 and 10')
elif(a % 2 == 0) and (a % 10 != 0):
    print('2')
elif(a % 2 != 0) and (a % 10 == 0): 
    print('10')
else:
    print('0')