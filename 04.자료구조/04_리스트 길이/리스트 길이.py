#리스트 길이란, 리스트에 저장된 아이템 개수를 뜻한다.

#len()

students = ['홍길동', '박찬호', '이용규']

slength = len(students)
print('length of students: {}'.format(len(students)))

# len() 과 반복문을 이용하면 리스트의 아이템 조회가 가능하다

for i in range(len(students)):
    print('i : {}'.format(i))
    print('students[{}] : {}'.format(i, students[i]))


# len() 함수는 리스트의 개수뿐만 아니라 문자열의 길이도 알 수 있다.

str = '정원국'
print('{}'.format(len(str)))


for i in range(3):   # 이거를 len 함수를 이용해서 아래와 같이 편하게 바꿀수 있다. (리스트 안에 아이탬이 많을 경우 )
    print(students[i])

slength = len(students)
for i in range(len(students)):
    print(students[i])


# llen()과 반복문을 이용하면 리스트의 아이템 조회가 가능하다.

n = 0
while n < slength:
    print('n : {}'.format(n))
    print('students[{}] : {}'.format(n, students[n]))
    n+=1

# 그냥 아이탬만 순서대로 출력하고 싶을때

for item in students :
    print(item)


