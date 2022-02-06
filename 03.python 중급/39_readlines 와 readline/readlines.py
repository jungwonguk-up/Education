#readlines 모든 글을 읽어온다. 리스트 형태로 반환해서 출력


uri = 'C:/Users/jcc96/Desktop/coding/'

with open (uri + 'score.txt', 'r') as f:
    lanlist = f.readlines()

print(f'lanlist: {lanlist}')
