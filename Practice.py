'''
sum = 0
numbers = 0
num = int(input('num:'))
while num != 0:
    numbers += 1
    sum += num
    num = int(input('num:'))
print(sum/numbers)

tCost = 0
while True:
    price = float(input('price:'))
    if(price > 1500):
        tCost += price * 0.92
    elif (price < 0):
        break
    else:
        tCost += price
print(tCost)

a = 1
b = 0
n = int(input('num:'))
while(a < n):
    t = a
    a += b
    b = t
    print(t)
'''
p = input('Write your new password:')
c = input('Rewrite it:')
check = ''
while check == False:
    while(len(p) < 8):
        print('Too short!')
        p = input('Rewrite your password!')
    
