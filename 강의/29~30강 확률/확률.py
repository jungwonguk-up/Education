#4장의 꽝카드와 3장의 선물 카드중 꽝2개와 선물 1장을 뽑을 확률은?


def profun() : #함수를 정의 한다.
    numn = int(input('numn 입력: '))
    numr = int(input('numr 입력: '))

    resultp = 1
    resultr = 1
    resultc = 1

    for n in range(numn, (numn - numr), -1 ):
        resultp = resultp *n 
    print('resultp : {}'.format(resultp))

    for n in range( numr, 0, -1):
        resultr = resultr *n
    print('resultr: {}'.format(resultr))

    resultc = int(resultp / resultr)
    print('resultc: {}'.format(resultc))

    return resultc #return으로 데이터를 반환 받는다


sample = profun()   # 전체 확률
print('sample: {}'.format(sample))

event1 = profun()   #꽝 나오는거
print('event1: {}'.format(event1)) 

event2 = profun()   # 선물 나오는거
print('event2: {}'.format(event2))

probability = (event1 * event2) / sample # 확률 구함

print('probability: {}%'.format(round(probability * 100, 2)))   # round로 감싼부분 >>> 소수점 둘째짜리 까지 표현