inputnumber = int(input('0���� ū ���� �Է� :'))  # �����ϱ� int ���


for number in range(1, inputnumber + 1):  #�÷��� 1�� �� �ϴ°���? / range = �ݺ����� / for? 
     if inputnumber % number == 0:  # % = ������ / == ���� / : �̳� ����? /  �������� 0�� ����  
         print ('{}�� ���: {}'. format(inputnumber, number)) #format �տ� .�� �� ��������? / format �� ���ϴ¾���? 
    