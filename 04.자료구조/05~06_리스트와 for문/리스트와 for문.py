# for문을 이용하면 리스트의 아이템을 자동으로 참조할 수 있다.

studentcsnts = [ [1,19], [2, 20], [3, 22], [4, 18 ], [ 5, 21]]

for classno, cnt in studentcsnts: # claasno 와 cnt 에 각각 리스트안의 리스트가 매칟된다.
    print('{}학급 학생수 : {}'.format(classno, cnt))

for i in range (len(studentcsnts)):
    print('{}학급 학생수 : {}'.format(studentcsnts[i][0], studentcsnts[i][1]))
