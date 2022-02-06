def cmtomm(n):
    return round(n * 10, 3) #소수점 3번째 자리에서 끊어줌
    
def cmtoinch(n):
    return round(n * 0.393, 3) 

def cmtom(n):
    return round(n * 0.01, 3) 

def cmtoft(n):
    return round(n * 0.032, 3) 

if __name__ == '__main__' :
    print(f'10cm: {cmtomm(10)}mm')
    print(f'10cm: {cmtoinch(10)}inch')
    print(f'10cm: {cmtom(10)}m')
    print(f'10cm: {cmtoft(10)}ft')