#if~elif문 : 여러 조건식 결과에 따라 실행

# examplescore = int(input(''))
# grades= ''


# if examplescore >= 90:
#     grades = 'a'

# elif examplescore >= 80:
#     greades = 'b'

# elif examplescore >= 70:
#     greades = 'c'

# print(grades)

print('1. a (3.5) \t 2. b(3.0) \t 3. c(2.0) ')

user = int(input(' : '))

if user == 1:
    print('메뉴 : 1')
    print('가격 : 3.5')
if user == 2:
    print('메뉴 : 2')
    print('가격 : 3.0')
if user == 3:
    print('메뉴 : 3')
    print('가격 : 2.0')

