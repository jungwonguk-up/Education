#writelines()는 리스트(list) 또는 튜플 데이터를 파일에 쓰기 위한 함수이다.

# languages = ['c/c++', 'java']

# uri = 'C:/Users/jcc96/Desktop/coding/'

# for item in languages:
#     with open (uri + 'languages.txt', 'a') as f:
#         f.write(item)
#         f.write('\n')


languages = ['c/c++', 'java']

uri = 'C:/Users/jcc96/Desktop/coding/'

# writelines 를 쓰면 반복문 없이 가능하다
with open (uri + 'languages.txt', 'a') as f:
    f.writelines(item + '\n' for item in languages)  #languages에 있는 item을 뽑아서 반복하는데 개행을 추가한다


scoredic = {'kor' : 85, 'eng' : 90}

for ke in scoredic.keys(): # keys 가 명령어가 따로 있는건가?
    with open (uri + 'scor.txt', 'a') as f:
        f.write(ke + '\t' + str(scoredic[ke])+ '\n') # key 는 문자고 / scoredic[key] 는 숫자인건가? 이게 무슨 명령어지?

with open (uri + 'scores.txt', 'a') as f:
    print(scoredic, file = f) # scoredic을 전부 그대로 쓴다

    # [] 이거는 리스트인데 {} 요놈은 뭐지? 


