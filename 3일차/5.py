def average_of_4_number(n1, n2, n3, n4):
    return (n1+n2+n3+n4)/4

num1 = int(input("첫번째 수를 입력하시오."))
num2 = int(input("두번째 수를 입력하시오."))
num3 = int(input("세번째 수를 입력하시오."))
num4 = int(input("네번째 수를 입력하시오."))

average = average_of_4_number(num1, num2, num3, num4)
print("4개의 평균은 %d입니다."%average)