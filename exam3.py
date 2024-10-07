year = int(input("년도 입력 : "))

if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0) :
    print(str(year) + "년은 윤년입니다.")
else :
    print(str(year) + "년은 평년입니다.")
print('-' * 20)
# 점수를 1개 입력받아서 학점을 출력하세요
# 학점은 A~F 
# if - else 만을 사용
jumsu = int(input('학점을 입력하세요 : '))

if jumsu >= 90 : print("A 학점")
else :
    if jumsu >= 80 : print("B 학점")
    else :
        if jumsu >= 70 : print("C 학점")
        else :
            if jumsu >= 60 : print("D 학점")
            else : print("F 학점")
        
        
        