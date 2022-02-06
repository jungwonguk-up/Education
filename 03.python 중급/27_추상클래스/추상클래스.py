# 추상클래스 = 상위 클래스에서 하위 클래스에 메서드 구현을 강요한다.

from abc import ABCMeta
from abc import abstractmethod

class AirPlane():

    @abstractmethod
    def flight(self):  #아무것도 구현하지 않고 pass함
        pass
        
    
    def forward(self):
        print('전진')


    def backward(self):
        print('후진')

class Airliner(AirPlane):

    def __init__(self,c):
        self.color = c
    
    def flight(self):  #여기서 이걸 꼭 해줘야만 함 / 위에서 정의를 안해서
        print('400km/h')


al = Airliner('red')
al.flight()
al.forward()
al.backward()