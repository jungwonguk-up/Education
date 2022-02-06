# 간단한 함수는 lamda 로 표현하면 쉽게 해결 가능하다

# def calculator(n1, n2):
#     return n1 + n2

# returnvalue = calculator(10, 20)
# print(f'returnvalue: {returnvalue}')

calculator = lambda n1, n2 : n1 + n2
returnvalue = calculator(10,20)
print(f'returnvalue: {returnvalue}')

