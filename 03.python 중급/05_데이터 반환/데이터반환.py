def calculator(n1, n2):
    result = n1 + n2

    return result


print(calculator(10,20))  #calculatr 함수에 10, 20을 넣고 수행한 값을 return을 통해서 다시 받아서 계산값을 프린팅한다
returnvalue = calculator(10,20) # 함수로 변수 지정
print(f'returnvalue: {int(returnvalue / 2) }') # 변수 프린트


#함수가 return을 만나면 실행을 종료한다

def dividenumber(n):

    if n % 2 == 0:
        return '짝수'
    else:
        return '홀수'

returnvalue = dividenumber(4)
print(returnvalue)


