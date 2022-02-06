#예외처리 = 예상하지 못한 예외가 프로그램 전체 실행에 영향이 없도록 처리함

# 예외 발생 예상 구문을 try ~ except로 감싼다

n1 = 10; n2 = 0

try:
    print(n1 / n2)

except:

    print ('예외발생')


print ( n1 + n2 )

nums = []

n = 1
while n < 6:

    try:
        num = int(input('   : ' ))
    except:
        print ( '예외')
        continue    #다시 위로 올려서 밑에줄이 실행 안되게 하고 재입력 하게 함

    nums.append(num)
    n += 1

print(f'nums: {nums}')
