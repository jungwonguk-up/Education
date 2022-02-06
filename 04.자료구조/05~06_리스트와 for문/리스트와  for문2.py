# for 문과 if문을 이용해서 과락 과목 출력하기

minsocre = 60
scores = [
    ['국어', 58],
    ['영어', 77],
    ['수학', 89],
    ['과학', 99]]

for item in scores:
    if item[1] < minsocre:
        print('과락 과목 : {}, 점수: {}'.format(item[0], item[1]))

for subject, score in scores:
    if score < minsocre:
        print('과락 과목 : {}, 점수: {}'.format(subject, score))

for subject, score in scores:
    if score >= minsocre: continue
    print('과락 과목 : {}, 점수: {}'.format(subject, score))

        