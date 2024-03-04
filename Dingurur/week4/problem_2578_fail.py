board = [list(input().split()) for _ in range(5)]
calling = []
for _ in range(5):
    calling += list(input().split())

cnt=0
bingo = False
def findbingo(board):
    global cnt, bingo
    tcnt = 0
    scnt = 0
    ascnt = 0
    for i in range(5):
        for j in range(5):
            if cnt == 3:
                bingo = True
                break
            if all(type(elem) != str for elem in board[i]):
                cnt += 1
            if board[i][i]==0:
                scnt+=1
                if scnt ==5:
                    cnt+=1
            if board[i][4-i]==0:
                ascnt+=1
                if ascnt ==5:
                    cnt+=1
for idx, elem in enumerate(calling) :
    for i in range(5):
        for j in range(5):
                if board[i][j]==elem:
                    board[i][j]=1
                    findbingo(board)
                    if bingo:
                        print(idx)
