import random

Num = int(input())
if 0< Num and Num <= 30000:
    Lst = [Num]

    randomNum = random.randint(1, Num)

    if randomNum<=Num :
        Lst.append(randomNum)
        second = randomNum
        while 1:
            temp = Num - second
            if temp<0:
                break
            Lst.append(temp)
            Num = second
            second = temp
        print(len(Lst))
        print(*Lst)
    else :
        print(*Lst)