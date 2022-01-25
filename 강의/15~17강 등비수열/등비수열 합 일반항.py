# 등비수열 합 공식 : sn = a1 * (1-r^n) / (1-r)
inputn1 = int(input('a1 입력: '))
inputr = int(input('공비 입력: '))
inputn = int(input('n 입력: '))

sumn = 0

sumn = inputn1 * (1-(inputr ** inputn)) / (1 - inputr)  # ^ = ** 이다.
print('{}번째 항까지의 합: {}'.format(inputn, int(sumn)))