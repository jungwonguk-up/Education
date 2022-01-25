#16장 등비수열 복습

inputa1 = int(input('a1 입력: '))
inputr = int(input('공비 입력: '))
inputn = int(input('n 입력'))

value = 0
sumn = 0
n = 1

while n <= inputn:
    if n == 1 :
        value = inputa1
        sumn += value
        print('{}번째 항까지의 합: {}'. format(n, sumn))
        n += 1
        continue

    value *= inputr
    sumn += value
    print('{}번째 항까지의 합: {}'.format(n, sumn))
    n += 1

print('{}번째 항까지의 합: {}'.format(n, sumn))