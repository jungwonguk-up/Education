#sn = a1 * (1-r^n) / (1-r)

inputnumber = int(input('첫번째 항 : '))
inputr = int(input('공차 : '))
inputn = int(input('항의 수 : '))

sum = inputnumber * (1 - (inputr ** inputn))/ (1 - inputr)

print('{}번째 항까지의 합: {} '.format(inputn, int(sum)))