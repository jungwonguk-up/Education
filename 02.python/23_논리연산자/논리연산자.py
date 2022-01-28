# 논리연산자 : TRUE , FALSE 를 이용한 연산

# AND 항상 둘다 만족해야함
# OR 어느거 하나만 만족하면됨
# NOT >>> 현재 상태를 부정

age = int(input('나이 : '))

vaccine = (age<20) or (age >= 60)

print('age: {}, vaccine: {}'.format(age, vaccine))
