num1 = int(input('1보다 큰 정수 입력: ')) # 가정, 두번째 수가 첫번째 보다 크다
num2 = int(input('1보다 큰 정수 입력: ')) # 만약 더 작은수 넣으면? 이상해짐 / 이 가정도 코딩으로 커버 안되나?

maxnum = 0

for i in range ( 1, (num1+1)) : # 1부터 num1+1 까지 반복을 실행 / num1과 num2사이의 숫자는 알 필요가 없다.
                                # 결국 최대 공약수를 찾는거니까 / 1부터 num1 까지의 숫자중에서 수행하면 되는거임
    if num1 % i == 0 and num2 % i == 0:
        print ( '공약수: {}'.format(i))
        maxnum = i # format(i)에 저장된 수 중에 가장 큰 수를 뽑아냄


print('최대공약수: {}'.format(maxnum))

