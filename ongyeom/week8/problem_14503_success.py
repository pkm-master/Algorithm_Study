dir = [(-1,0),(0,1),(1,0),(0,-1)]

N,M = map(int,input().split())
r,c,d = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr[r][c] = 2
cnt = 1
while arr[r][c] != 1:
    fe = 0
    for _ in range(4):
        d -= 1
        if d == -1: d=3
        nr = r + dir[d][0]
        nc = c + dir[d][1]
        if arr[nr][nc] == 0:
            r = nr
            c = nc
            arr[r][c] = 2
            cnt += 1
            fe = 1
            break
    if not fe:
        r += dir[d-2][0]
        c += dir[d-2][1]

print(cnt)