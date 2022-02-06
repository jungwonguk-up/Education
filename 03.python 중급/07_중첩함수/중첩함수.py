# 중첩함수에서 내부 함수를 함수 밖에서 호출할 수 없다.

# def out_funtion():
#     print('123')

#     def in_function():
#         print('234')

#     in_function() # 함수내에서 호출 가능

# in_function() # 함수 외부에선 불가능 인식 못함

def calculator(n1, n2, operator):
    
    def addcal():
        print(f'덧셈 연산: {n1 + n2}')

    def subcal():
        print(f'뺄셈 연산: {n1 - n2}')

    def mulcal():
        print(f'곱셈 연산: {n1 * n2}')

    def divcal():
        print(f'덧셈 연산: {n1 / n2}')

    if operator == 1:
        addcal()
    if operator == 2:
        subcal()
    if operator == 3:
        mulcal()
    if operator == 4:
        divcal()

while True:
    num1 = float(input(' 실수 1:'))
    num2 = float(input(' 실수 2:'))
    operatornum = int(input('1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈, 5.종료'))

    if operatornum == 5:
        print('end')
        break

    calculator(num1, num2, operatornum)