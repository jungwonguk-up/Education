class passwordlengthshortexception(Exception):
    def __init__(self, str):
        super().__init__ (f'{str}: 길이 5 미만')

class passwordlengthlongexception(Exception):
    def __init__(self, str):
        super().__init__ (f'{str}: 길이 1o 초과')

class passwordlengthwrongexception(Exception):
    def __init__(self, str):
        super().__init__ (f'{str}: 잘못된 비밀번호')


adminpw = input('input password: ')

try:
    if len(adminpw) < 5:
        raise passwordlengthshortexception(adminpw)
    if len(adminpw) > 10:
        raise passwordlengthlongexception(adminpw)
    if len(adminpw) != 'admin1234':
        raise passwordlengthwrongexception(adminpw)

except passwordlengthshortexception as e1:
    print (e1)

except passwordlengthlongexception as e2:
    print (e2)

except passwordlengthwrongexception as e3:
    print (e3)