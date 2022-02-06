n,k = map(int,input().split())
npac = 1
list = []

for i in range(1,(n+1)): #i는 1~ n 까지 반복
    
    for j in range(1, (i+1)): # i 가 골라지면 j는 1~i까지 곱함  = i! 구하기
    
        npac = npac * j

    if npac - i <= k : # 
        list.append(n)

print('{}'.format(len(list)))

# 문제점 : for반복을 끝내고 if 로 넘어가는게 문제가 있는거 같다
# 해결책 : ???

#1부터 N까지의 수를 임의로 배열한 순열은 총 N! = N×(N-1)×…×2×1 가지가 있다.

# 모든 1 ≤ i ≤ N에 대해서 |P[i] - i| ≤ K를 만족하는 순열 P의 개수를 구하는 프로그램을 작성하시오.