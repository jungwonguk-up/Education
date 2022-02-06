import random
uri = uri = 'C:/Users/jcc96/Desktop/coding/'

def writenumbers(nums):
    for idx, num in enumerate(nums):  # enumerate 사용 법 알아야함
        with open(uri + 'lotto.txt', 'a') as f:
           if idx < len(nums) - 2 :           #idx 랑 len(nums) 랑 비교를 왜 하는거지?
                f.write(str(num) + ', ')
           elif idx == len(nums) - 2 :
                f.write(str(num))
           elif idx == len(nums) - 1 :
                f.write('\n') # \n 개행
                f.write(str(num))
                f.write('\n') 


rnums = random.sample(range(1, 46), 7)
print(f'rnums: {rnums}')


writenumbers(rnums)