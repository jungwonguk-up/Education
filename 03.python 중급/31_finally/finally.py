# finally  =  예외 발생과 상관없이 항상 실행한다.

try:
    inputdata = input("   : ")
    numint = int(inputdata)

except:
    print('exception')
    numint = 0

else:
    if numint % 2 == 0:
        print ('짝수')
    else:
        print ( '홀수')

finally:
    print(f'{inputdata}')
    
