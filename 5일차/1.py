def price(amount):
    if 0 <= amount < 10:
        return 100 * amount
    elif 10 <= amount < 30:
        return 95 * amount
    elif 30 <= amount < 100:
        return 90 * amount
    elif 100 <= amount:
        return 85 * amount
    else:
        print("잘못된 입력입니다.")


mount = int(input("구매할 상품 개수를 입력하시오. : "))
print("상품의 가격은 %d입니다."%(price(mount)))