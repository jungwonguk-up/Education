# raise 키워드를 이용하면 예외를 발생시킬 수 있다.

def divcalculator(n1,n2):

    if n2 != 0:
        print(f'{n1} / {n2} = {n1 / n2 }')
    else:
        raise Exception('나눌수 없음')

num1 = int(input('num1 : '))
num2 = int(input('num2 : '))

try:
    divcalculator(num1,num2)
except Exception as e:
    print(f'{e}')
