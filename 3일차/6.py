def print_absolute():
    number = int(input("정수를 입력하시오 :"))
    # print("%d의 절대값:"%number,abs(number))
    if number < 0:
        print(number * -1)
    # print(-number)

print_absolute()