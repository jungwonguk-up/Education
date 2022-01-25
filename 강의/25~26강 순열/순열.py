numN = int(input('numN 입력: '))
numR = int(input('numR 입력: '))
result = 1

for n in range(numN, (numN-numR), -1): # range 에서 뒤에꺼는 바로 그 직전값까지 수행하는거임
    print('n : {}'.format(n))
    result = result *n

print('result: {}'.format(result))

