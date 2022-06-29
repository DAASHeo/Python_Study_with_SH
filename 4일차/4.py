from turtle import speed


class Car:
    carname = ""
    speed = 0

Car_1 = Car()
Car_1.carname = "아우디"
Car_1.speed = 0
Car_2 = Car()
Car_2.carname = "벤츠"
Car_2.speed = 30

def present(Carvalue1, Carvalue2):
    print(Carvalue1.carname,"의 현재 속도는",Carvalue1.speed,"입니다.")
    print(Carvalue2.carname,"의 현재 속도는",Carvalue2.speed,"입니다.")

present(Car_1,Car_2)