inputm = int(input('m : '))

#n = 0 #정수 n
sum = 0 # 시그마 n
a2 = [] #짝수만 모아두는 리스트
a3 = 0 #약수

#약수 구하고 시그마 하기.
for n in range( 1, inputm+ 1):
    if inputm % n == 0: # 나눠서 나머지가 0이되는거를 선별해서 약수를 구한다.  // n이 들어가면 안되는데?
       a3 = n 
       sum += a3
       print(sum)
    if sum % 2 == 0:
        a2.append(n) #시그마 값이 짝수이면 a2에 리스트 업
        print(a2)


print('{}'.format(len(a2))) # a2의 갯수를 카운팅해서 출력

#len / count


