#조건문 안에 또다른 조건문

# 왠만하면 너무 많은 조건문은 사용하지 않는다. 1~2단계정도만 사용

score = int(input(' '))

if score < 60 :
    pass

else:
    if score >= 90:
        print ("a")
    elif score >= 80:
        print ("b")
    
