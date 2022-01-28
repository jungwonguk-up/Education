#n번째 항까지의 합
#an = a1 + (n-1)d
#sn = n ( a1 + an) / 2
inputnumber = int(input('첫번째 항 : '))
inputd = int(input('공차 : '))
inputn = int(input('항의 수 : '))

sum = 0

sum = inputn * (inputnumber + inputnumber + (inputn -1) * inputd) / 2

print(int(sum))