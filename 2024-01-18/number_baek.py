# 숫자를 CRUD를 하는 프로그램
# front(사용자와 대화, view)와 baek(crud...처리)이 섞여있다
# 숫자추가,숫자출력,합계평균,숫자삭제 기능
# 데이터 자체는 원래 백이 아니라 database에서 관리
# front는 사용자와 입출력하는 view를 담당(터미널,웹,안드로이드,아이폰)
# baek은 처리를 담당하고 view에 상관없이 재사용하고 싶다
# baek을 재사용 하려면 baek에는 절대로 view 관련 코드가 없어야 한다

numbers = []

def save(num:int)->bool:
    if isinstance(num,int)==False:
        return False
    numbers.append(num)
    return True

def find_all()->list:
    return numbers

def delete(num:int)-> bool:
    if isinstance (num,int)==False:
        return False
    for item in numbers:
        if item==num:
            numbers.remove(item)
        return True
    return False
