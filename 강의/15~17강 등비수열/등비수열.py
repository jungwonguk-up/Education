# n번째 항의 값을 출력하는 프로그램 / 등비 수열

inputn1 = int(input('a1 입력: '))
inputr = int(input('공비 입력: '))
inputn = int(input('n 입력: '))

valuen = 0

n = 1

while n <= inputn:  #while 문은 n을 통해서 무한루프에 빠지지 않게 해주는게 일반적이다.
    if n == 1:
        valuen = inputn1
        print('{}첫번째 항의 값: {}'.format(n, valuen))
        n += 1
        continue

    valuen *= inputr
    print('{}번째 항의 값: {}'.format(n, valuen))
    n += 1

print ('{}번째 항의 값: {}'.format(inputn, valuen))