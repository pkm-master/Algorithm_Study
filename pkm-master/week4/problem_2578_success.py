def ch(check):
    global line
    if check.count('X')==5:
        line+=1

board = [list(map(int,input().split())) for _ in range(5)]
moder = []
for _ in range(5):
    moder.extend(list(map(int,input().split())))

for n in range(len(moder)):
    line = 0
    el = moder[n]
    for i in range(5):
        for j in range(5):
            if board[i][j] == el :
                board[i][j] = 'X'
    
    for i in range(5) :
        check1 = [board[i][j] for j in range(5)]
        ch(check1)
    
    for j in range(5):
        check2 = [board[i][j] for i in range(5)]
        ch(check2)
    
    check3 = [board[i][i] for i in range(5)]
    ch(check3)
    
    check4 = [board[i][4-i] for i in range(5)]
    ch(check4)

    if line >=3 :
        break

print(n+1)