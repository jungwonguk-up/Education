# 8C3 , 7C5 프로그램 만들기
# nPr/r!
from tkinter import N


numn = int(input('numn 입력: '))
numr = int(input('numr 입력: '))
resultp = 1
resultr = 1
resultc = 1

for n in range(numn, (numn-numr), -1):
    print('n : {}'.format(n))
    resultp = resultp * n 

print('resultp: {}'.format(resultp))

for n in range(numr, 0, -1):
    print('n : {}'.format(n))
    resultr = resultr *n

print('resultr: {}'.format(resultr))

resultc = int(resultp / resultr)
print('resultc: {}'.format(resultc))
