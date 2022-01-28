N = int(input())

n=2
for n in range(2, N+1):
    if N%n == 0:
        print(n)
        N/=n
    

    else:
        n+=1