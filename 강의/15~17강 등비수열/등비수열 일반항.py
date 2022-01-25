# 등비수열 일반항으로 구하기

inputn1 = int(input('a1 입력: '))
inputr = int(input('공비 입력: '))
inputn = int(input('n 입력: '))

#an = a1*r^(n-1)
valuen = 0
valuen = inputn1 * (inputr ** (inputn - 1 ))
print('{}번째 항의 값: {}'.format(inputn, valuen))

