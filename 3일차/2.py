import random

def lottery():
    count = 0
    # random.seed(1789) 다시 알아보자
    print("추첨된 로또 번호 ==> ",end="")
    while(count < 6):
        print(random.randint(1,45)," ",end="")
        count += 1

print("** 로또 추첨을 시작합니다. **")
print(" ")
lottery()