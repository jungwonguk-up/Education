inputnumber = int(input('0보다 큰 정수 입력 :'))  # 정수니까 int 사용


for number in range(1, inputnumber + 1):  #플러스 1은 뭐 하는거지? / range = 반복구문 / for? 
     if inputnumber % number == 0:  # % = 나누기 / == 같다 / : 이놈 뭐지? /  나머지가 0인 숫자  
         print ('{}의 약수: {}'. format(inputnumber, number)) #format 앞에 .은 왜 찍은거지? / format 은 뭐하는애지? 
    