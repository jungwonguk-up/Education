# 예외 담당 클래스 exception


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
    except Exception as e:
        print (f'exception: {e}')  # exception 클래스
        continue   

    nums.append(num)
    n += 1

print(f'nums: {nums}')
