# 4명의 친구가 원탁 테이블에 앉을 수 있는 순서

n = int(input('친구 수 입력: '))
result = 1
for i in range(1, n):
    result *= i

print('result: {}'.format(result))

