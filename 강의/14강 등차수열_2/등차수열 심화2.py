#sn = n(a1 + an) / 2

inputN1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력:')) 

valueN = inputN1 + (inputN - 1) * inputD
sumN = inputN * (inputN1 + valueN) /2
print('{}번째 항까지의 합: {}'.format(inputN, sumN)) # 파이선에서 나누기는 항싱 실수가 됨
print('{}번째 항까지의 합: {}'.format(inputN, int(sumN))) # int로 정수로 바꿔줌5
