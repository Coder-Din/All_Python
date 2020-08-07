'''
a = 3
b = 4.7
round3D = b/a
print(round(round3D, 3))
print(b % a)
print(b ** a)

n = 7
k = 15
aEach = k // n
pRem = k%n
print('Each one will get', aEach, 'apples')
print(pRem, 'apple is left')
'''
num1 = int(input('Write a 3-digit number:'))
sumNum1 = num1//100
num2 = num1%100
sumNum2 = num2//10
sumNum3 = num2%10
sumTotal = sumNum1 + sumNum2 + sumNum3
print(sumTotal)




