num1 = int(input('1보다 큰 정수 입력: '))
num2 = int(input('1보다 큰 정수 입력: '))
maxnum = 0

for i in range (1, (num1 +1)):
    if num1 % i ==0 and num2 % i ==0:
        print('공약수: {}'.format(i))
        maxnum = i #maxnum에 최대 공약수 저장 / ex10) 최대공갹수가 저장소에 들어가는게 
                   #1,2,5,10 이 순서로 치환되서 들어가서 마지막 10이 나오는건가?


print('최대공약수: {}'.format(maxnum))

minnum = (num1 * num2) // maxnum # 두 수를 곱한후에 최대 공약수로 나눠주면 최소 공배수가 된다.

print('최소공배수: {}'.format(minnum) )