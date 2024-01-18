import number_baek as n
while True:
    print('****************')
    print('1.숫자추가')
    print('2. 숫자출력')
    print('999. 종료')

    selet= input('매뉴선택:')
    if selet=='1':
        num = int(input('숫자입력:')) 
        n.save(num)
    elif selet=='2':
        print(n.find_all())
    elif selet=='999':
        print('감사합니다')
    break