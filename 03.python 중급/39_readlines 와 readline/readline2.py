scoreDic = {}

uri = 'C:/Users/jcc96/Desktop/coding/'

with open(uri + 'scoretest.txt', 'r') as f:
    line = f.readline()

    while line != '':
        tempList = line.split(':') #split = :를 기준으로 구분해서 리스트로 저장함
        scoreDic[tempList[0].strip('"')] = int(tempList[1].strip('\n')) # strip은 ()안에 있는걸 잘라서 없애버림 # 이 줄이 이해가 안감
                                                            # int로 가져와서 \n은 어차피 표현이 안됨
                                                            # key 랑 value랑 구분해서 표현해야함
        line = f.readline()

    print(f'{scoreDic}')

