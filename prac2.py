kor = int(input('국어점수 입력 : '))
eng = int(input('영어점수 입력 : '))

tot = kor + eng
avg = tot / 2
grade = None
err = None

if avg >= 90 and avg <= 100 : grade = 'A'
elif avg >= 80 and avg < 90 : grade = 'B'
elif avg >= 70 and avg < 80 : grade = 'C'
elif avg >= 60 and avg < 70 : grade = 'D'
elif avg >= 0 and avg < 60 :  grade = 'F'
else : err = 'E'

print()    # 1줄 넘김
if err != 'E' : 
    print('총점 = %s\n평균 = %s\n학점 = %s' 
          %(tot, avg, grade))
else :
    print('점수 입력이 잘못되었습니다.')