num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))

if num2 > num1 :
    num1, num2 = num2, num1  # 두변수값 변경
    '''
    # 두변수값 변경
    temp = num1
    num1 = num2
    num2 = temp
    '''
    #pass   # 임시 명령문으로 형식만 갖추는 명령어
    
print('큰값 : %d, 작은값: %d' %(num1, num2))

