# 주로 while 로 사용
# while n <= endnum   이게 트루일경우 실행
#      print(n)
#      n += 1

from tkinter import N


num = int(input('희망 구구단 : '))

n=1
while n < 10:
    result = num*n
    print(result)
    n += 1