# 파일 모드는 파일을 어떤 목적으로 OPEN할지 정한다
# 'w' 쓰기전용 - 파일 있으면 덮어씌움
# 'a' 쓰기전용 - 파일 있으면 덧붙임
# 'x' 쓰기전용 - 파일 있으면 에러 발생
# 'r' 읽기전용 - 파일 없으면 에러 발생

uri = 'C:/Users/jcc96/Desktop/coding/'

def writeNumber(n):

    file = open(uri + 'number.txt', 'a') # 누적해서 써야하므로 a
    file.write(str(n)) # 숫자를 문자로 바꿔서 넣는다
    file.write('\n') # 개행해준다.
    file.close()

inputNumber = int(input(' 정수입력 :'))
for number in range(2, (inputNumber + 1)):
    flag = True
    for n in range(2,number):
        if number % n == 0:
            flag = False
            break
    if flag :
        writeNumber(number)
