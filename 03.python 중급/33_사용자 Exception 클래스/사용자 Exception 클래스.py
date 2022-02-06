class notusezerowxception(Exception):

    def __init__(self, n):
        super().__init__(f'{n}은 사용할 수 없습니다')

def divcalculator(num1,nu2):

    if num2 == 0:
        raise notusezerowxception(num2)
    else:
         print(f'{num1} / {num2} = {num1 / num2}')

num1 = int(input(' num1 : '))
num2 = int(input(' num2 : '))

try:
    divcalculator(num1, num2)
except notusezerowxception as e:
    print(e)
