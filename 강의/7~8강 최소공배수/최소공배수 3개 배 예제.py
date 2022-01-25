ship1 = 12; ship2 = 36; ship3 = 48;
maxday = 0

for i in range(1, (ship1 + 1)):
    if ship1 % i == 0 and ship2 % i == 0: # %나누는거랑 / 로 나누는거랑 무슨차이지?
        maxday = i
    
print('최대공약수: {}'.format(maxday))

minday = (ship1 * ship2) // maxday # 나누셈은 //
print('{}, {}의 최소 공배수: {} '.format(ship1, ship2, minday))

newday = minday # ship 1과 ship2의 최소공배수를 구하고 그 최소 공배수와 ship3 의 최소 공배수를 다시 구한다.

for i in range(1,(newday + 1)):
    if newday % i ==0 and ship3 % i == 0:
        maxday = i
print ( '최대공약수: {}'.format(maxday))

minday = (newday * ship3) // maxday
print('{}, {}, {}의 최소공배수: {}'.format(ship1, ship2, ship3,  minday))

#이렇게 두번에 걸친 작업 말고 한번에 하는 방법 없나?
# 배의 배송날짜를 입력하게 하는것도 수정해보자