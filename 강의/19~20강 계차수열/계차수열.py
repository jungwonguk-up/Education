# 계차수열
# an = 3, 7, 13, 21, 31, 43, 57
#        4, 6, 8, 10, 12, 14

inputan1 = int(input('a1 입력: '))
inputan = int(input('an 입력: '))

inputbn1 = int(input('b1 입력: '))
inputbd = int(input('bn  공차 입력: '))

valuean = 0
valuebn = 0

n = 1

while n <= inputan:


    if n == 1:
        valuean = inputan1
        valuebn = inputbn1 
        print('an의 {}번째 항의 값: {}'.format(n, valuean))
        print('bn의 {}번째 항의 값: {}'.format(n, valuebn))
        n +=1
        continue

    valuean = valuean + valuebn
    valuebn = valuebn + inputbd 
    print ('an의 {}번째 항의 값: {}'.format(n, valuean))
    print ('bn의 {}번째 항의 값: {}'.format(n, valuebn))
    n +=1

print('an의 {}번째 항의 값: {}'.format(inputan, valuean))
print('bn의 {}번째 항의 값: {}'.format(inputan, valuebn))

