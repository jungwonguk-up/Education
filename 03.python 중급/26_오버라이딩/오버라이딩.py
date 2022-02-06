#오버라이딩 = 하위 클래스에서 상위 클래스의 매서드를 재정의 하는것

class Robot:

    def __init__(self, c, h, w):
        self.color = c
        self.height = h
        self.weight = w
    
    def fire(self):
        print('미사일 발사')

    def printRobotInfo(self):
        print(f'self.color: {self.color}')
        print(f'self.height: {self.height}')
        print(f'self.weight: {self.weight}')

class NewRobot(Robot) :
    def __inint__(self, c, h, w):
        super().__init__(c,h,w)

    def fire(self):
        print('레이저 발사')

myRobot = NewRobot('red', 200, 300)
myRobot.printRobotInfo()
myRobot.fire()