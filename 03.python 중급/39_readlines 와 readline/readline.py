# readline 은 한 행씩 읽어서 문자열로 반환



uri = 'C:/Users/jcc96/Desktop/coding/'

with open (uri + 'score.txt', 'r') as f:
    line = f.readline()

    while line != '':
        print(f'line: {line}', end= '')
        line = f.readline()
