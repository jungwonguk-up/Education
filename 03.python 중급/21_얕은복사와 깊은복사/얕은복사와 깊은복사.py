# 얕은복사 = 객체 주소를 복사하는것으로 객체 자체가 복사되진 않는다

# 깊은복사 = 객체 자체를 복사하는것으로 또 하나의 객체가 만들어진다

from tkinter import N


class temcls:

    def __init__(self, n, s):
        self.number = n
        self.str = s

    def printclasinfo(self):
        print(f'self.number: {self.number}')
        print(f'self.str: {self.str}')

#얕은 복사
tc1 = temcls(10, 'hello')
tc2 = tc1

tc1.printclasinfo()
tc2.printclasinfo()

tc2.number = 3.14
tc2.str = 'bye'

tc1.printclasinfo()
tc2.printclasinfo()

# 깊은 복사
import copy
tc3 = temcls(10, 'hell')
tc4 = copy.copy(tc3)

tc3.printclasinfo()
tc4.printclasinfo()

tc3.number = 3.14
tc3.str = 'bye'

tc3.printclasinfo()
tc4.printclasinfo()