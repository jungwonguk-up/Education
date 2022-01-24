inputnumber = int(input('0보다 큰 정수 입력: '))

for number in range(2, (inputnumber + 1)): #소수에 1은 포함이 안되므로 2부터 시작
    # number 라는 변수에 담아준다. for 반복문, range 범위
    flag = True #flag 는 뭐하는놈이지? / True 꼭 대문자 여야함/ 
    for n in range (2, number): #n이라는 변수에 담겠다
        if number % n == 0: #inputnumber의 약수를 찾는 과정 ex) 6이면 1,2,3,6
            flag = False # EX) 4를 넣으면 1~4까지 숫자로 4를 나누는것이므로 2가 나머지 0을 만드니까 FALSE로 들어간다.
            break # 루프를 멈춤
                           # 5를 넣으면 1~5까지 숫자로 5를 나누는것이므로 5외엔 나머지를 0을 만드는게 없으니 TRUE 
    if (flag):
        print('{} : 소수!!'.format(number)) # TRUE 가 나오면 소수

    else:
        print('{} : \t\t 합성수!!'.format(number)) # FALSE가 나오면 합성수