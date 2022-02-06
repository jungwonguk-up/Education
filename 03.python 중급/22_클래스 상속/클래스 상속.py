#클래스는 또 다른 클래스를 상속해서 내 것처럼 사용할 수 있다.

class normalcar:

    def drive(self):
        print(' move')
    
    def back(self):
        print(' back')

class turbocar(normalcar): #()안에 클래스를 넣으면 상속받아서 위에 기능을 사용할 수 있다.
        
        def turbo(self):
            print(' turbo')

myturbocar = turbocar()

myturbocar.turbo()
myturbocar.drive()
myturbocar.back()
