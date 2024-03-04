board = [list(input().split()) for _ in range(5)]
calling = []
for _ in range(5):
    calling += list(input().split())

cnt=0
scnt=0
while cnt<=3:
    for idx, elem in enumerate(calling) :
        for i in range(5):
            for j in range(5):
                if board[i][j]==elem:
                    board[i][j]=1
                if board[i].count(1)==5:
                    cnt += 1
                if board[j].count(1)==5:
                    cnt += 1
    #         # if board[i][i]==0:
    #         #     scnt+=1
    #         #     if scnt ==5:
    #         #         cnt+=1

    print(board)
    print(cnt)