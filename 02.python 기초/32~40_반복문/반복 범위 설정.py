# range 함수 
# for i in range ( 1,11,1) 1부터 10까지 1 씩 증가)
# 괄호 안은 시작 , 끝 , 단계 순서
# 단계가 1인경우는 단계 생략 가능 range (1, 11)
# 시작이 0인경우 생략 가능 for i in range(11)

start = int(input(' : '))
end = int(input(' : '))

for i in range(start,(end+1),3):
    print(i)
    