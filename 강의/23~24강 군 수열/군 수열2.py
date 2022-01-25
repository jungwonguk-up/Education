# 1/1, 1/2, 2/1, 1/3, 2/2, 3/1, .... 군수열 구하기

inputn = int(input('n항 입력: '))

flag = True
n = 1; nCnt = 1; searchnc = 0; searchnp = 0
while flag:

    for i in range(1, (n + 1)):
        if i == n :
            print('{}/{} '.format(i, (n-i + 1)), end= '')
        
        else:
            print('{}/{}, '.format(i, (n-i + 1)), end= '')

        nCnt += 1
        if (nCnt > inputn):
            searchnc = i
            searchnp = n - i + 1
            flag = False
            break
    print()
    n += 1

print('{}항: {}/{}'.format(inputn, searchnc, searchnp))
