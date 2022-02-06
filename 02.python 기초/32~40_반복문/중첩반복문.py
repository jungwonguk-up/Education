#반복문 안에 또 다른 반복문 선언

for i in range(1,10): # 1~10 까지 반복
    for j in range(i): # 0~i까지 반복
        print('*', end='') #별 치고 개행안함
    print() # 개행

# 반복문은 2~3단계 까지만 쓴다

for i in range (10,0,-1): # 10부터 0 전까지 -1 만큼 가라
    for j in range(i):
        print('1', end='')
    print()
    