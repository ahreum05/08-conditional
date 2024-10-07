num1 = float(input("첫 번째 수 : "))
num2 = float(input("두 번째 수 : "))
result = None
op = input("연산자 : ")

if op == "+":   result = num1 + num2
elif op == "-": result = num1 - num2
elif op == "*": result = num1 * num2
elif op == "/":
    if bool(num2) :  # 0인지 검사
        result = num1/num2
    else : result = "E"

if result != 'E' :
    print("%s %s %s = %s" %(num1, op, num2, result)) 
else : print("0으로 나눌수 없습니다.")


