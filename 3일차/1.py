import datetime
import time

def split1(char1):
    year,month,day = char1.split("/")
    total = 0
    int(year)
    int(month)
    int(day)

start = input("시작 날짜(연/월/일) -->")
split1(start)
now = datetime.datetime.now()
print(start+"부터 오늘(",now.year,"/",now.month,"/",now.day,") 까지는", ,"일이 지났습니다.")
print("그리고 오늘은")