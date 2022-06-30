def sum(n1,n2,gap):
    total = 0
    for i in range(n1,n2+1,gap):
        total += i
    return total

num1 = int(input("첫 번째 숫자를 입력하세요 :"))
num2 = int(input("두 번째 숫자를 입력하세요 :"))
gap = int(input("더할 숫자를 입력하세요 :"))

total = int(sum(num1,num2,gap))

print("%d+%d+...+%d는 %d입니다."%(num1, num1+3,num2, total))
    