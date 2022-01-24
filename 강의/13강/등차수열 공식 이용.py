inputN1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력:')) 

valueN = 0

# an = a1 + (n-1)d

valueN = inputN1 +(inputN - 1) * inputD
print('{}번째 항의 값: {}'.format(inputN, valueN))
