# 반복문 for을 이용해서 팩토리얼 계산



inputn = int(input('n 입력: '))

result = 1
for n in range(1, inputn + 1):
    result *= n

print('{} 팩토리얼: {}'.format(inputn, result))


