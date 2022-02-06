import unitconversion as uc

inputnumber = int(input('길이(cm) 입력: '))

returnvalue = uc.cmtomm(inputnumber)
print(f'returnvalue: {returnvalue}mm')
