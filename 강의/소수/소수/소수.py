for number in range (2, (inputnumber +1)): #�Ҽ��� 1�� ������ �ȵǹǷ� 2���� ����
    flag = true # flag�� ���ϴ³�����? (���� ���尰���ѵ�)
    for n in range(2, number): # n �̰� ����?
        if number % n == o:
            flag - False
            break # break �Ƹ��� ���ߴٴ� ���ε�

        if (flag):
            print('{} : �Ҽ�!!'.format(number))
                  
        else:
            print('{} : �ռ���!!'.format(number))

         
        
