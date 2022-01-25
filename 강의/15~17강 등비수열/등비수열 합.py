#n번째 항까지의 합을 출력하는 프로그램

inputn1 = int(input('a1 입력: '))
inputr = int(input('공비 입력: '))
inputn = int(input('n 입력: '))

valuen = 0
sumn = 0
n = 1
while n <= inputn:

    if n == 1:
        valuen = inputn1
        sumn += valuen
        print('{}번째 항까지의 합: {}'.format(n, sumn))
        n +=1
        continue # continue 를 하면 바로 if로 올라감

    valuen *= inputr
    sumn += valuen
    print('{}번째 항까지의 합: {}'.format(n, sumn))
    n +=1

print('{}번째 항까지의 합: {}'.format(inputn, sumn))

