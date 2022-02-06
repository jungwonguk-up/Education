file = open('C:/Users/jcc96/Desktop/coding/test.txt', 'r', encoding = 'UTF8')  # 인고딩이 안맞아서 UTF9 해줌
                                                                               # 추가적으로 이게 뭔지 알아봐야함

str = file.read() 
print(f'str: {str}')

str = str.replace('Python', '파이썬', 2) # replace 를 통해서 python을 파이썬으로 2개만 바꾼다.
print(f'str: {str}')

file.close()

file = open('C:/Users/jcc96/Desktop/coding/test.txt', 'w')  
file.write(str)
file.close
                                                                              
