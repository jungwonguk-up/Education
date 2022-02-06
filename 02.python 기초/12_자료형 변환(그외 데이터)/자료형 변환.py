var1 = 'True'
var2 = 'False'

print(type(var1))
print(type(var2))

var1 = bool(var1)   #이건 TRUE 로 인식
var2 = bool(var2)    # 이것도 TRUE 로 인식 / 데이터가 있으면 True기 때문이다.

print(var1 + var2)  #True + True 이므로 2가 나옴
print(type(var1 + var2))