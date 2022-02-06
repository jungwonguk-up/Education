from ipaddress import collapse_addresses


class Car: # 클래스 선언

    def __init__(self, col, len): # 생성자,속성
        self.color = col
        self.length = len

    def doStop(self): #기능
        print('stop')

    def doStart(self): #기능
        print('start')
    
    def printcarinfo(self):
        print(f'self.color: {self.color}')
        print(f'self.length: {self.length}')



car1 = Car('red', 200)
car2 = Car('bule', 300)


car1.printcarinfo()
car2.printcarinfo()
