# 문제 1
식재료별_칼로리={
    '밀가루':364,
    '피망' : 20.1,
    '올리브' : 115,
    '돼지고기' : 242.1
}

# 문제 2, 문제 3
def kcal(food,mount):
    if(food in 식재료별_칼로리):
        return 식재료별_칼로리.get(food) * (mount/100)
    else:
        return 0

식재료별_칼로리['치즈'] = 402.5 ##문제 3
food = input("음식의 종류를 입력하세요 :")
mount = int(input("섭취량을 입력하세요 :"))
result = kcal(food,mount)

print("총 칼로리는",result)

