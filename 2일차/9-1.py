from itertools import count
from unicodedata import name

def kiosk():
    name=input("당신의 이름을 입력해주세요")
    coffee=int(input(name+"씨, 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4:에스프레소)"))
    offer(coffee)
    print(name+"씨~ 커피 여기 있습니다.")
    

def offer(coffee):
    if (coffee == 1):
        print("#1.(자동으로)뜨거운 물을 준비한다.")
        print("#2.(자동으로)종이컵을 준비한다.")
        print("#3.(자동으로)에스프레소를 탄다.")
        print("#4.(자동으로)물을 붓는다.")
        print("#5.(자동으로)스푼으로 젓는다.")

    elif (coffee == 2):
        print("#1.(자동으로)뜨거운 우유를 준비한다.")
        print("#2.(자동으로)종이컵을 준비한다.")
        print("#3.(자동으로)에스프레소를 탄다.")
        print("#4.(자동으로)우유를 붓는다.")
        print("#5.(자동으로)스푼으로 젓는다.")

    elif (coffee == 3):
        print("#1.(자동으로)뜨거운 우유를 준비한다.")
        print("#2.(자동으로)종이컵을 준비한다.")
        print("#3.(자동으로)에스프레소를 탄다.")
        print("#4.(자동으로)우유를 붓는다.")
        print("#5.(자동으로)스푼으로 젓는다.")
        print("#6.(자동으로)우유 거품을 올린다.")
        print("#7.(자동으로)시나몬을 올린다.")

    elif (coffee == 4):
        print("#1.(자동으로)종이컵을 준비한다.")
        print("#2.(자동으로)에스프레소를 탄다.")

    else:
        print("잘못된 주문입니다. 처음부터 다시 진행해주세요.")
        kiosk()

count = 0

while(count < 5):
    kiosk()
    count += 1