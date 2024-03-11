board = [[0]*1001 for _ in range(1001)]

n = int(input())
for N in range(n):
    x,y,delx,dely = map(int,input().split())
    for i in range(delx):
        for j in range(dely):
            board[i+x][j+y] = N+1

for N in range(n):
    cnt = 0
    for i in range(1001):
        cnt+=board[i].count(N+1)
    print(cnt)
