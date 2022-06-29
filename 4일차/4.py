class Car():
    speed = 0
    def p(speed, name):
        print(name,"===>현재의 속도(슈퍼 클래스)",speed)

class sedan(Car):
    def p(speed, name):
        print(name,"===>현재의 속도(서브 클래스)",speed)

class Sonata(sedan):
    pass


car1 = Car.p(200, "트럭")
car2 = sedan.p(150, "승용차")
car3 = Sonata.p(150, "소나타")
