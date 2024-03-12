C, R = map(int, input().split()) #C가 가로, R이 세로
K = int(input())
arr = [[0]*C for _ in range(R)]
start = (R-1,0)
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

cnt=1
flag=False
y, x = start
arr[y][x]=1
result=0
if R*C<K:
    print(result)
else :
    for _ in range(K):
        for dir in dirs:
            while cnt<=K and not flag:
                ny, nx = y+dir[0], x+dir[1]
                if ny<0 or R<=ny or nx<0 or C<=nx:
                    y = ny-dir[0]
                    x = nx-dir[1]
                    break
                if 0<=ny<R and 0<=nx<C and arr[ny][nx]==0:
                    arr[ny][nx]=1
                    cnt+=1
                    y,x=ny,nx
                    if cnt==K:
                        result = (R-y, 1+x)
                        flag=True
                        break
                continue

        if flag:
            break   
    print(result)