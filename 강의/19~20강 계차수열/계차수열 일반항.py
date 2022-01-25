# 계차수열
# an = 3, 7, 13, 21, 31, 43, 57
#        4, 6, 8, 10, 12, 14

#bn = 2n+2
#bsn = (k-1)(4+2(k-1)+2)/2
#    = k^2 + k -2
# k^2 + k -2 = an -3
# an = n^2 + n + 1

inputan1 = int(input('a1 입력: '))  # 첫항은 필요하지도 않음
inputan = int(input('an 입력: '))

valuean = inputan ** 2 + inputan + 1
print('an의 {}번째 항의 값: {}'.format(inputan, valuean))
