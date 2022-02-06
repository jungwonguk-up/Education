# with ~ as 문을 이용하면 파일닫기 (close) 를 생량 가능하다
uri = 'C:/Users/jcc96/Desktop/coding/'

with open(uri + '001.txt', 'a') as f:
    f.write('hye')


with open(uri + '001.txt', 'r') as f:
    print(f.read())

