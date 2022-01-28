# 반복문 while을 이용해서 팩토리얼 계산



from tkinter import N


inputn = int(input('n 입력: '))

result = 1
n =1
while n <= inputn:
    result *= n 
    n += 1

print('{} 팩토리얼: {}'.format(inputn, result))

# 왜  while문보다 for문이 더 적합하다고 한거지?