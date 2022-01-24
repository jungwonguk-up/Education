inputnumber = int(input('1보다 큰 정수 입력: '))

n=2
while n <= inputnumber: # while 문을 사용해서 반복 / 입력숫자까지 반복한다 / <= ?
    if inputnumber % n == 0: # 나머지가 0인경우 ex) 12넣으면
        print('소인수: {}'.format(n)) # ex) 2를 일단 format으로 빼낸다.
        inputnumber /= n # 인풋 넘버에 나눠진 값이 다시 들어가고 위에 if문으로 가서 다시 진행
                         # ex) 6을 다시 인풋넘버에 할당해줌
    else:
        n +=1

