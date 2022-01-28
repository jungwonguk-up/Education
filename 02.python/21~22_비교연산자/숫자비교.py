# > , >= , < , <= , == , !=

# != 같지 않다

num = 10; num2 = 5 #변수를 같은 줄에 쓸때 ; 로 변수의 끝을 말해줄 수 있다.

inputnum1 = int(input('첫번째 숫자 : '))
inputnum2 = int(input('두번째 숫자 : '))

print('{} > {} : {}'.format(inputnum1, inputnum2, (inputnum1>inputnum2)))