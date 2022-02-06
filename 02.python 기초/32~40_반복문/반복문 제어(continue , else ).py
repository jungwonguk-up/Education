# 반복 실행중 continue 를 만나면 실행을 생략하고, 다음 반복 실행문으로 넘어간다.

for i in range(100):
    if i % 7 != 0 :
        continue
    print ('{}는 7의 배수입니다.'.format(i))

    