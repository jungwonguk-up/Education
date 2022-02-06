# 함수 호출 시 함수에 데이터를 전달할 수 있다.

def great(customer): # customer  =매개변수
    print(f'{customer}')

great('홍길동') # 홍길동 = 인수

#인수와 매개변수 개수는 일치해야한다

def add(n1,n2):
    print(f'{n1}+{n2}={n1+n2}')

add(10,20)

# 갯수가 정해지지 않았을때는 *을 넣는다

def pnumber(*numbers):
    for number in numbers :
        print(number , end='   ')    # \t랑 end랑 같이 쓰면 안되나??   /  숫자를 띄워서 표기하고 싶은데
    print()
pnumber()
pnumber(10)
pnumber(10,20)
pnumber(10,20,30)



