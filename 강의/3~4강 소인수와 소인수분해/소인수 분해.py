# 소인수분해를 해서 어떤걸 곱해줘야 어떤수의 제곱수가 되는지 판별하는법
inputnumber = int(input('1보다 큰 정수 입력: '))

n=2
searchnumbers = [] # 리스트 선언, 리스트는 대괄호로 선언한다 
while n <= inputnumber:    
    if inputnumber % n ==0:
        print('소인수: {}'.format(n)) 
        if searchnumbers.count(n) == 0: # searchnumbers를 갯수를 확인했더니 0개이면
            searchnumbers.append(n)   #0개이면 그 n의 갯수를 추가한다.
        elif searchnumbers.count(n) == 1: # n이 한개가 있으면?
            searchnumbers.remove(n) #한개가 있으면 지워버린다. 두개가 되서 거듭제곱이 되니까 알 필요 없다.
        
        inputnumber /= n
    else:
        n +=1

print('searchnumbers: {}'.format(searchnumbers))
