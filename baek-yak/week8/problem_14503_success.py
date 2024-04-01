# 14503 로봇청소기
# 방향
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 방문 확인
visited = [[0]*m for _ in range(n)]
visited[r][c] = 1
ans = 1

while True:
    cnt = 0            
    for _ in range(4):  
        d = (d+3) % 4
        ni = r + di[d]
        nj = c + dj[d]

        # 범위 안에, 빈 칸이고, 청소할 수 있다면!
        # 청소하고, 카운트하고, 현재 위치 갱신, cnt 변경!
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
            if visited[ni][nj] == 0:
                visited[ni][nj] = 1
                ans += 1
                r = ni
                c = nj
                # 청소함
                cnt = 1
                break

    if cnt == 0:
        # 네 방향 모두 청소를 할 수 없을 때
        # 후진 했을 때 벽 break
        # 벽이 아니라면 위치갱신
        if arr[r-di[d]][c-dj[d]] == 1:
            print(ans)
            break
        else:
            r, c = r-di[d], c-dj[d]