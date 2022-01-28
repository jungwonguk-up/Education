# 시그마 함수 σ(n)은 정수 n의 약수의 합을 구하는 함수이다.
# 예를 들어, σ(2) = 1+2 = 3이고, σ(6) = 1+2+3+6 = 12, σ(12) = 1+2+3+4+6+12 = 28 이다.
# m이 주어졌을 때, 1 ≤ n ≤ m인 모든 n의 σ(n) 중에서 값이 짝수인 것이 몇 개 있는지 구하는 프로그램을 작성하시오.

m = int(input("입력: "))

def solution(n): 
        return sum([i for i in range(1, n+1) if n % i == 0])
# m = int(input("입력: "))
cn = []

for o in range(1,m+1):
    k = solution(o)
    if k % 2 == 0:
        cn.append(k)
        o=+1
    else:
        o=+1
print(len(cn))