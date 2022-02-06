# open() = 파일 열기
# read() or write() = 읽기 또는 쓰기
# close() = 파일닫기

file = open('C:/Users/jcc96/Desktop/coding/test.txt', 'w') # w는 쓰기라는뜻  r 은 읽기라는 뜻  
                                                        # 주소 복사하면 \를 /로 바꿔줘야함
                                                        # .txt 붙여줘야 텍스트 파일됨
                                                        # w는 기존의 글자를 전부 지우고 덮어쓴다

strCnt = file.write('hello world') # 글자갯수인 11이 출력됨
print(f'shrCnt: {strCnt}')

file.close()

# 왜 파일이 없지???
