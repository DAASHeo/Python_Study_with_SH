#2
tt = ((1, 2, 3),
      (4, 5, 6),
      (7, 8, 9))

# for i in tt:
#     print(i)

# (1, 2, 3)
# (4, 5, 6)
# (7, 8, 9)
# 우리가 원하는 출력값이 아님

for i in range(0,3):
    for k in range(0,3):
        print(tt[i][k],end="")
        print(" ")

