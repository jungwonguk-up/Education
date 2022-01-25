#1,1,2,1,2,3,1,2,3,4,1,2,3,4,5.... 이 수열의 n번째 항의 값 출력하는 프로그램

inputn = int(input('n항 입력: '))

flag = True # flag 얘는 그냥 변수인가?
n = 1; nCnt = 1; searchn = 0 # 변수 = 다음에 ; 넣고 안넣고 차이는 뭐지? / nCnt 이건 항의 숫자를 담는 n
while flag:

    for i in range (1, (n+1)): # 이 for문이 군 안에서의 반복임
        if i == n: #각항의 끝의 항이 같으면
            print('{} '.format(i), end= '') # end 이건 뭐야 >> 이게 개행 막아준다는데 흠..
        
        else:         # 각항의 끝의항이 같지 않으면                
            print('{}, '.format(i), end='')

        nCnt += 1
        if (nCnt > inputn):
            searchn = i
            flag = False # while 문 빠져나오는것
            break #for문 빠져나오는것
    print()  # 뭘 프린트하는지 안넣어도 되는건가? / # 개행?
    n += 1

print('{}항: {}'.format(inputn, searchn))
