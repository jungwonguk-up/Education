#모듈 = 누군가 이미 만들어놓은 기능

import operator
age = 31
num1 = 8
num2 = 3

print ('{}+{}:{}'.format(num1,num2,operator.add(num1,num2)))
print ('{}-{}:{}'.format(num1,num2,operator.sub(num1,num2)))
print ('{}*{}:{}'.format(num1,num2,operator.mul(num1,num2)))
print ('{}/{}:{}'.format(num1,num2,operator.truediv(num1,num2)))
print ('{}%{}:{}'.format(num1,num2,operator.mod(num1,num2)))
print ('{}//{}:{}'.format(num1,num2,operator.floordiv(num1,num2)))
print ('{}**{}:{}'.format(num1,num2,operator.pow(num1,num2)))

vaccine = operator.or_(operator.lt(age, 20), operator.ge(age, 65))
print('age: {}, vaccine: {}'.format(age, vaccine))