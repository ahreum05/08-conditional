jumsu = int(input('학점을 입력하세요 : '))

if jumsu >= 90 : print("A 학점")
else :
    if jumsu >= 80 : print("B 학점")
    else :
        if jumsu >= 70 : print("C 학점")
        else :
            if jumsu >= 60 : print("D 학점")
            else : print("F 학점")
print('-' * 20)
            
# elif : else if를 축약한 명령문
if jumsu >= 90 : print("A 학점")
elif jumsu >= 80 : print("B 학점")
elif jumsu >= 70 : print("C 학점")
elif jumsu >= 60 : print("D 학점")
else : print("F 학점")

