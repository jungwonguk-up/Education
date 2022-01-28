N = int(input( ))

n =2

for i in range ( 2, (N+1)):
    if N%n == 0:
        print(int(n))
        N /= n
    else:
        n+=1



#inputnumber = int(input('1 부터 10000000 까지의 정수 N : '))

#n=2
#while n <= inputnumber: 
#    if inputnumber % n == 0: 
#        print('소인수: {}'.format(n))
#        inputnumber /= n 
                         
#    else:
#        n +=1
