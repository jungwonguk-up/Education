# 함수 이용해서 팩토리얼 계산

inputn = int(input('n 입력: '))

def factorialfun(n):
    if n == 1 :              # 만약 n 이 1이면 종료
        return 1

    return n * factorialfun(n -1) # n이 1이 아니면 n에 팩토리얼 펑션 (n-1) 을 곱하고 다시 수행

print('{} 팩토리얼: {}'.format(inputn, factorialfun(inputn))) # 마지막에 왜 함수에 inputn을 주는거지?

#재귀함수 : 나 자신을 다시 호출

# inport math 이걸 사용하면 왠만한 계산은 다 함수셋팅이 되어있다.
# print('{}팩토리얼: {}'.format(inputn, math.factorial(inputn)))
