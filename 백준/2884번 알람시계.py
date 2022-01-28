set_h = int(input()) #시간입력
set_m = int(input()) # 분입력

# 1시간은 60분이기때문에 이를 조건에 넣어줘야함

if set_m >= 45 :
    print('{}:{}'.format(set_h,(set_m-45) ))

if set_h > 0 :
    print('{}:{}'.format((set_h-1),(set_m+15))) # 60분더하고 -45분해서 + 15분
    
elif set_h == 0:
    print('{}:{}'.format((23),(set_m+15)))

