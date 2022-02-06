# % >> 나눗셈 결과 나머지만 구함 

# // >>>  몫만 구하는놈임

# divmod() 함수  = 몫과 나머지를 한번에 구함

num1=10
num2=3

result = divmod(num1,num2)
print('{}'.format(result))
print('{}'.format(result[0]))
print('{}'.format(result[1]))