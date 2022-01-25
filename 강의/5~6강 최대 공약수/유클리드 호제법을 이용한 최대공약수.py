num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))

temp1 = num1; temp2 = num2

while temp2 > 0 : #temp2 = 나누는 수 가 0 보다 클때까지 계속 반복
    temp = temp2 # temp에 일단 temp2를 할당한다. 임시로
    temp2 = temp1 % temp2 #temp2를 temp1을 temp2로 나눈값으로 저장
    temp1 = temp #temp1을 아까 임시로 저장했던 temp = temp2 값으로 저장


print('{},{}의 최대공약수: {}'.format(num1, num2, temp1))

for n in range(1, (temp +1)):
    if temp1 % n ==0:
        print('{},{}의 공약수: {}'.format(num1, num2, n))

        # 이것도 작은거부터 넣어야함 / ex) 8,16 으로 하면 큰거부터 넣었을때 약수 2가 빠지는데 왜지?


