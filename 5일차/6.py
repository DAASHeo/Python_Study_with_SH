from itertools import count


count = 0
while (count < 5):
    print(" " * (4-count),end="")
    print(("*" * count)+"*"+("*" * count),end="")
    print(" " * (4-count))
    count += 1

while (count-1 > 0):
    print(" " * (6 - count),end="")
    print(("*" * (count - 2))+"*"+("*" * (count - 2)),end="")
    print(" " * (6 - count))
    count -= 1