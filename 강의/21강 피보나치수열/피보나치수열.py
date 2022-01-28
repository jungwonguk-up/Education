#피보나치 수열

inputn = int(input('n 입력: '))

valuen = 0
sumn = 0

valuepren2 = 0
valuepren1 = 0

n = 1

while n <= inputn:
    if n == 1 or n == 2:
        valuen = 1
        valuepren2 = valuen
        valuepren1 = valuen
        sumn += valuen
        n += 1
    
    else:
        valuen = valuepren2 + valuepren1
        valuepren2 = valuepren1
        valuepren1 = valuen
        sumn += valuen
        n += 1

print('{}번째 항의 값: {}'.format(inputn, valuen))
print('{}번째 항까지의 합: {}'.format(inputn, sumn))

# 이건 수열이 무조건 1부터만 시작한다는 한계가 있음. 내가 원하는 수부터 시작하게 하려면?



