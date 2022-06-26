##문제 4
day_of_week={'월','화','수','목','금','토','일'}
work={'월','화','수','목','금'}
rest={'토','일'}

##문제 5
def is_holiday(date):
    if (date in day_of_week):
        print(date in work)
    else:
        print("잘못된 입력입니다.")

date = input("'월','화','수','목','금','토','일' 중 하루를 선택하세요")
is_holiday(date)
