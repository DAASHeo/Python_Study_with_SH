def calc(num1, sum, num2):
    if(sum == '+'):
        total = num1 + num2
        print("##계산기 :",num1,'+',num2,'=',total)
    elif(sum == '-'):
        total = num1 - num2
        print("##계산기 :",num1,'- ',num2,'=',total)
    elif(sum == '*'):
        total = num1 * num2
        print("##계산기 :",num1,'*',num2,'=',total)
    elif(sum == '/'):
        if (num2 == 0):
            print("0으로 나누면 안 됩니다.ㅠㅠ")
        else:
            total = num1 / num2
            print("##계산기 :",num1,'/',num2,'=',total)
    elif(sum == '**'):
        total = num1 ** num2
        print("##계산기 :",num1,'**',num2,'=',total)
    else:
        print('올바르지 않은 연산자입니다.')

num1 = int(input("첫 번째 수를 입력하세요 :"))
sum = input("계산을 입력하세요(+, -, *, /, **) :")
num2 = int(input("두 번째 수를 입력하세요 :"))

calc(num1, sum, num2)