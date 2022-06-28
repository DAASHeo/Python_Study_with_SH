def triangle(width, height):
    return width * height / 2
    
w = int(input("밑변을 입력하세요."))
h = int(input("높이를 입력하세요."))
area = triangle(w,h)

print("삼각형의 넓이는 %d이다."%area)


