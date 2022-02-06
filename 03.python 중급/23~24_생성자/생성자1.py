# 객체가 생성될 때 생성자를 호출하면 __init__() 가 자동 호출된다

class calculator:

    def __init__(self):
        print('calculator')


cal = calculator()

# __init__() 가 속성을 초기화 한다

class calculator2:

    def __init__(self, n1 , n2):
        print('calculator')
        self.num1 = n1
        self.num2 = n2



cal = calculator2(10,20) # 초기화 진행
print(f'{cal.num1}')
print(f'{cal.num2}')


# 다른 초기화 방법

class calculator3:

    def __init__(self):
        print('calculator')
        self.num1 = 100 # n1, n2 필요없이 그냥 고정된 100, 200으로 초기화
        self.num2 = 200



cal = calculator3() # 초기화 진행
print(f'{cal.num1}')
print(f'{cal.num2}')


# 상속받을때 상위 클래스 초기화 하는법
class p_class:

    def __init__(self, pnum1, pnum2):
        print('p_class')

        self.pnum1 = pnum1
        self.pnum2 = pnum2
    
class c_class(p_class):

    def __init__(self, cnum1, cnum2):
        print('c_class')

        #p_class.__init__(self,cnum1,cnum2) # 이게 지금 뭘 한거지?
        super().__init__(cnum1, cnum2) # 슈퍼는 상위 클래스를 불러오는거임 /  self를 쓰지 않아도 된다.

        self.cnum1 = cnum1
        self.cnum2 = cnum2

cls = c_class(10,20)
