# try ~ except ~ else
# else sms 예외가 발생하지 않은 경우 실행하는 구문

# 이중문일떄 continue 활용 해보기 !!


nums = []

n = 1
while n < 6:

    try:
        num = int(input('  값 : ' ))
    except:
        print ( '예외')
            #예외가 발생하면 다시 위로 올려서 밑에줄이 실행 안되게 하고 재입력 하게 함 / try 로 다시 보냄
    
    else:
        if num % 2 == 0 :
            nums.append(num)
            n += 1
        
        else : 
            print('홀수 입니다.')
            print (' 다시 입력하세요')
              # 이 continue 는 어디로 다시 보내는거지?? 필요한 놈인가?
                      # 위에나 아래나 둘다  n+=1 이 걸려있지 않고 else일때만 카운팅 되는거니까 
                      # 사실상 continue는 필요 없는거 아닌가

print(f'nums: {nums}')
