inputn = int(input()) # n입력

valuen = 0
sumn = 0

valuepren2 = 0
valuepren1 = 0

n = 1

while n <= inputn:
    if n == 1 or n == 2:
        valuen = 1
        valuepren2 = valuen
        valuepren1 = valuen
        sumn += valuen
        n += 1
    
    else:
        valuen = valuepren2 + valuepren1
        valuepren2 = valuepren1
        valuepren1 = valuen
        sumn += valuen
        n += 1
        

print('{}'.format(valuen))
