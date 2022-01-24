for number in range (2, (inputnumber +1)): #소수에 1은 포함이 안되므로 2부터 시작
    flag = true # flag는 뭐하는놈이지? (변수 저장같긴한데)
    for n in range(2, number): # n 이건 뭐야?
        if number % n == o:
            flag - False
            break # break 아마도 멈추다는 거인듯

        if (flag):
            print('{} : 소수!!'.format(number))
                  
        else:
            print('{} : 합성수!!'.format(number))

         
        
