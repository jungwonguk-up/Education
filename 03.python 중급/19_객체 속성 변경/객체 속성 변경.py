#객체 속성은 변경할 수 있다.

class newgenerationpc:

    def __init__(self, name, cpu, memory, ssd):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd

    def doexecel(self):
        print('excel run')
    
    def dophotoshop(self):
        print( ' phtoshop run')
    
    def printpcinfo(self):
        print(f'self.name: {self.name}')
        print(f'self.name: {self.cpu}')
        print(f'self.name: {self.memory}')
        print(f'self.name: {self.ssd}')
       
mypc = newgenerationpc('mypc', 'i5', '16g', '500')
mypc.printpcinfo()

mypc.cpu = 'i9'
mypc.memory = '32g'
mypc.printpcinfo()