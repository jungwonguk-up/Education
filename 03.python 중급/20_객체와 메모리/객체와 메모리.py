# 변수는 객체의 메모리 주소를 저장하고 이를 이용해서 객체를 참조한다.

class robot:

    def __init__(self, color, height, weight):
        self.color = color
        self.height = height
        self.weight = weight
    
    def printrobotinfo(self):
        print(f'color: {self.color}')
        print(f'height: {self.height}')
        print(f'weight: {self.weight}')

rb1 = robot('red', 200, 80)
rb2 = robot('blue', 300, 120)
rb3 = rb1 # rb3에는 rb1의 메모리 주소값이 카피됨 "얕은 카피"


rb1.printrobotinfo()
rb2.printrobotinfo()
rb3.printrobotinfo()

rb1.color = 'gray'
rb1.height = '250'
rb1.weight = '100'

rb1.printrobotinfo()
rb2.printrobotinfo()
rb3.printrobotinfo()


