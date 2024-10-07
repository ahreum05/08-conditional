jumsu = 87

if jumsu >= 80 and jumsu < 90 :
    print('B 학점입니다.')
    print('열심히 하셨군요...')
    
# 점수를 1개 입력받아서 학점을 출력하세요
# 학점은 A~F
jumsu = int(input('학점을 입력하세요 : '))
if jumsu >= 90:
    print('A학점입니다.')
if jumsu >= 80 and jumsu < 90:
    print('B학점입니다.')
if jumsu >= 70 and jumsu < 80:
    print('C학점입니다.')
if jumsu >= 60 and jumsu < 70:
    print('D학점입니다.')
if jumsu < 60:
    print('F학점입니다.')
    
    