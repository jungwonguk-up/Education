n,x = map(int,input().split())
nlist = list(map(int,input().split()))
final = []

for i in range(n):
    if nlist[i] < x :
        print(nlist[i], end= ' ')
        # final.append(nlist[i]) # 그냥 = 을 하면 마지막 한개만 리스트에 올라가고 += 을 하면 오류가 뜸


# print(final)
