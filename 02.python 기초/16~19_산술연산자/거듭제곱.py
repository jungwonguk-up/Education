# 거듭제곱 >> **

num1 = 2
num2 = 3

result = num1 ** num2
print('result: {}'.format(result))

# 제곱근 >>   n**(1/m)

result2 = 2 ** (1/2)

print('result: {}'.format(result2))

# sqrt() 제곱근 구하기 >>> 2제곱근만 구할 수 있음

import math   #항상 이렇게 불러와야 쓸 수 있다.

print(math.sqrt(4))


# pow() 거듭제곱 구하기


n = 9000000
str_n = format(n, ',') #>> 이렇게 하면 3자리씩 끊어서 , 표시를 해준다
print(str_n,' 원')